 #-*- coding:utf-8 -*-
'''
RNN-LSTM 循环神经网络
''' 
"""
return_sequences控制返回类型
-True,返回所有输出序列,应为下一层需要处理过拟合,
-False,只返回输出序列的最后一个
在堆叠LSTM层是必须设置,最后一层LSTM不用设置
"""               
import tensorflow as tf

def network_model(inputs, num_pitch, weights_file=None):
    model = tf.keras.models.Sequential()
    #第一层得到神经元数512-LSTM
    model.add(tf.keras.layers.LSTM(
        512,  # LSTM 层神经元的数目是 512，也是 LSTM 层输出的维度
        input_shape=(inputs.shape[1], inputs.shape[2]),  # 输入的形状，对第一个 LSTM 层必须设置
        # return_sequences：控制返回类型
        # - True：返回所有的输出序列
        # - False：返回输出序列的最后一个输出
        # 在堆叠 LSTM 层时必须设置，最后一层 LSTM 可以不用设置
        return_sequences=True  # 返回所有的输出序列（Sequences）
    ))

    #Dropout丢弃30%,防止过拟合
    model.add(tf.keras.layers.Dropout(0.3))

    #第二层-LSTM
    model.add(tf.keras.layers.LSTM(512, return_sequences=True))
    model.add(tf.keras.layers.Dropout(0.3))

    #第三层-LSTM
    model.add(tf.keras.layers.LSTM(512))#return_sequences默认为False
    model.add(tf.keras.layers.Dense(256))#256个神经元的全连接层
    model.add(tf.keras.layers.Dropout(0.3))
    model.add(tf.keras.layers.Dense(num_pitch))#输出的数目等于所有不重复的音调的数目,音调数

    model.add(tf.keras.layers.Activation("softmax"))#用softmax激活函数计算每个音符的概率

    # 交叉熵计算误差,使用对循环神经网络适合的RMSProp优化器
    model.compile(loss="categorical_crossentropy", optimizer="rmsprop")

    if weights_file is not None: #如果是 生成 音乐时
        # 从 HDF5 文件加载所有神经网络层的参数(Weights)
        model.load_weights(weights_file)

    return model
