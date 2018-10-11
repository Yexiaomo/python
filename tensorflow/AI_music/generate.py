# -*- coding:utf-8 -*-
import numpy as np
import tensorflow as tf
import pickle

from utils import *
from network import *

# 以之前训练所得的最佳参数来生成音乐
def generate():
    #加载用于训练神经网络的音乐数据
    with open('music_data/notes', 'rb') as filepath:
        notes = pickle.load(filepath)

    pitch_names = sorted(set(item for item in notes))

    num_pitch = len(set(notes))

    network_input, normalized_input = prepare_sequences(notes, pitch_names, num_pitch)

    #载入之前训练时得到的最好的参数(最小loss),来生成神经网络模型
    model = network_model(normalized_input, num_pitch, "best-weight.hdf5")
    # 用神经网络来生成音乐数据
    prediction = generate_notes(model, network_input, pitch_names, num_pitch)
    #用使用预测的音乐数据生成MIDI文件,再转换成mp3
    create_music(prediction)

def prepare_sequences(notes, pitch_names, num_pitch):
    """
    为神经网络准备好供训练的序列
    """
    sequence_length = 100  # 序列长度

    # 创建一个字典，用于映射 音调 和 整数
    pitch_to_int = dict((pitch, num) for num, pitch in enumerate(pitch_names))

    # 创建神经网络的输入序列和输出序列
    network_input = []
    network_output = []

    for i in range(0, len(notes) - sequence_length, 1):
        sequence_in = notes[i: i + sequence_length]
        sequence_out = notes[i + sequence_length]

        network_input.append([pitch_to_int[char] for char in sequence_in])
        network_output.append(pitch_to_int[sequence_out])

    n_patterns = len(network_input)

    # 将输入的形状转换成神经网络模型可以接受的
    normalized_input = np.reshape(network_input, (n_patterns, sequence_length, 1))

    # 将 输入 标准化 / 归一化
    # 归一话可以让之后的优化器（optimizer）更快更好地找到误差最小值
    normalized_input = normalized_input / float(num_pitch)

    # 将期望输出转换成 {0, 1} 组成的布尔矩阵，为了配合 categorical_crossentropy 误差算法使用
    normalized_output = tf.keras.utils.to_categorical(network_output)

    return network_input,normalized_input

def generate_notes(model, network_input, pitch_names, num_pitch):
    """
    基于-序列音符用神经网络来生成新的音符
    """
    #从输入里随机选择一个序列,作为"预测"生成的音乐的起始点
    start = np.random.randint(0, len(network_input)-1)
    #在创建一个字典用于映射音调和整数
    int_to_pitch = dict((num, pitch) for num,pitch in enumerate(pitch))

    pattern = network_input[start]
    #神经网络实际生成的音调
    prediction_output = []

    #生成700个音调/音符
    for note_index in range(700):
        prediction_intput = np.reshape(pattern, (1,len(pattern)), 1)
        prediction_intput = prediction_intput / float(num_pitch)

        # 用载入了训练所得最佳参数文件的神经网络来预测/生成 新的音调/音符
        prediction = model.predict(prediction_intput, verbose=0)

        #取最大值的维度(类似One-hot编码)
        index = np.argmax(prediction)

        #将整数转成音调
        result = int_to_pitch[index]

        prediction_output.append(result)

        pattern.append(index)
        pattern = pattern[1:len(pattern)]

    return prediction_output

if __name__ == '__main__':
    generate()