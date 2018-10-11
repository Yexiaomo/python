# -*- coding:utf-8 -*-
"""
训练神经网络,将参数(weight)存入HDF5文件
"""
import numpy as np
import tensorflow as tf

from utils import *
from network import *

def train():
    notes = get_notes()
    #得到所有不重复的音调数目
    num_pitch = len(set(notes))
    
    network_input, network_output = prepare_sequences(notes, num_pitch)
    model = network_model(network_input, num_pitch)

    filepath = "weight-{epoch:02d}-{loss:.4f}.hdf5"

    #使用checkpoint(检查点)文件 
    checkpoint = tf.keras.callbacks.ModelCheckpoint(
                    filepath, #保存文件的路径
                    monitor = "loss",#监控对象是损失(loss)
                    verbose = 0,
                    save_best_only = True,#不替换最近的数值最佳的监控对象的文件
                    mode = 'min'#取损失最小的
                    )
    callbacks_list = [checkpoint]

    model.fit(network_input, network_output, epochs=100, batch_size=64, callbacks=callbacks_list)



def prepare_sequences(notes, num_pitch):
    """
    为神经网络准备好供训练的序列
    """
    sequence_len = 100 #设定为100
    #得到所有不同的音调名字
    pitch_names = sorted(set(item for item in notes))
    #创建字典,用映射音调和整数(训练)
    pitch_to_int =  dict((pitch, num) for num, pitch in enumerate(pitch_names))
    #创建神经网络输入序列和输出序列
    network_input = []
    network_output = []

    for i in range(0, len(notes) - sequence_len, 1):
        sequence_in = notes[i : i+sequence_len]
        sequence_out = notes[i+sequence_len]

        network_input.append([pitch_to_int[char] for char in sequence_in])
        network_output.append(pitch_to_int[sequence_out])

    n_patterns = len(network_input)
    #将输入序列的形状转成LSTM模型可以接受的
    network_input = np.reshape(network_input, (n_patterns, sequence_len, 1))

    #将输入标准化
    network_input = network_input / float(num_pitch)
    #将期望输出转成{0,1}组成布尔矩阵, 为了配合前面的误差算法
    network_output = tf.keras.utils.to_categorical(network_output)

    return network_input, network_output

if __name__ == "__main__":
    train()