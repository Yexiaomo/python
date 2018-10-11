# -*- coding:utf-8 -*-
'''
MIDI 相关函数
'''
import os
import subprocess
import pickle
import glob
from music21 import converter, instrument, note, chord, stream

def convertMidiToMp3():
    """
    将神经网络生成的 MIDI 文件转成 MP3 文件
    """
    input_file = 'output.mid'
    output_file = 'output.mp3'

    if not os.path.exists(input_file):
        raise Exception("MIDI 文件 {} 不在此目录下，请确保此文件被正确生成".format(input_file))

    print('将 {} 转换为 MP3'.format(input_file))

    """
    用 timidity 生成 mp3 文件
    # 注意：Windows 用户可能需要用其他命令来将 MIDI 文件转为 MP3 文件
    # 注意：Mac 用户貌似 libmp3lame 选项会出错，需要下载编译 libmp3lame，
    # 再重新编译 ffmpeg ：http://blog.csdn.net/qinggebuyao/article/details/20933497
    # 不过，Mac 用户直接用自带的 GarageBand（车库乐队）可以直接播放生成的 MIDI 文件，比 ffmpeg 生成的 MP3 音色更好
    """
    command = 'timidity {} -Ow -o - | ffmpeg -i - -acodec libmp3lame -ab 64k {}'.format(input_file, output_file)
    return_code = subprocess.call(command, shell=True)

    if return_code != 0:
        print('转换时出错，请查看出错信息')
    else:
        print('转换完毕. 生成的文件是 {}'.format(output_file))


def get_notes():
    """
    从所有midi文件读取note(音符)和chord(和弦)
    Note样例: A,B,A#,B#,G-
    chord样例: [B4 E5, G#5], [C5 E5]
    因为chord就是多个Note的集合,所以简单统称为Note
    """
    if not os.path.exists("music_midi"):
        raise Exception("包含所有 MIDI 文件的 music_midi 文件夹不在此目录下，请添加")
    notes = []
    #glob:匹配所有符合条件的文件,并以List返回
    for file in glob.glob("music_midi/*.mid"):
        stream = converter.parse(file)
        parts = instrument.partitionByInstrument(stream)
        
        if parts:
            notes_to_parse = parts.parts[0].recurse()
        else:
            notes_to_parse = stream.flat.notes

        for e in notes_to_parse:
            # 如果属于note类型,取音调
            if isinstance(e, note.Note):
                # 格式如  E6
                notes.append(str(e.pitch))
            elif isinstance(e, chord.Chord):
                #如果是和弦,转化成整数,如4.15.7
                notes.append('.'.join(str(n) for n in e.normalOrder))

    # 如果 data 目录不存在，创建此目录
    if not os.path.exists("music_data"):
        os.mkdir("music_data")

    with open('./music_data/notes', 'wb') as filepath:
        pickle.dump(notes, filepath)

    return notes

def create_music(prediction):
    """
    用神经网络预测的音乐数据来生成MIDI文件,再转成mp3文件
    """
    offset = 0 #偏移量
    output_notes = []
    #生成note音符或和弦对象
    for data in prediction:
        if('.' in data) or data.isdigit():
            notes_in_chord = data.split('.')
            notes = []
            for nc in notes_in_chord:
                new_note = note.Note(int(nc))
                new_note.storedInstruemnt = instrument.Piano()#创建钢琴对象
                notes.append(new_note)
            new_chord = chord.Chord(notes)
            new_chord.offset = offset
            output_notes.append(new_chord)
        else:
            new_note = note.Note(data)
            new_note.offset = offset
            new_note.storedInstruemnt = instrument.Piano()
            output_notes.append(new_note)

        #每次迭代都将偏移增加,这样才不会覆盖
        offset += 0.5

    # 创建音乐流
    midi_stream = stream.Stream(output_notes)
    # 写入MIDI文件
    midi_stream.write('midi', fp='output.mid')
    convertMidiToMp3()