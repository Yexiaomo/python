# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# # 下载并载入MNIST手写数字库 (55000张 * 28行 *28个)
# from tensorflow.examples.tutorials.mnist import input_data

# # one_hot 是一种独热码的编码形式
# mnist = input_data.read_data_sets('mnist_data', one_hot=True)
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# None 表示张量(tensor)的第一个维度可以是任何维度
input_x = tf.placeholder(tf.float32, [None, 28*28]) / 255 # 除以255 是得到灰度值范围
output_y = tf.placeholder(tf.int32, [None, 10])           # 输出: 10个数字的标签
input_x_images = tf.reshape(input_x, [-1, 28, 28, 1])     # 改变形状 28*28*1

# 从Test测试数据集里选取3000个手写数字的图片和对应标签
test_x = mnist.test.images[:3000]
test_y = mnist.test.labels[:3000]

# 第一层卷积
conv1 = tf.layers.conv2d(
            inputs = input_x_images,
            filters = 32,
            kernel_size = [5,5],
            strides = 1,
            padding = "same",
            activation = tf.nn.relu
            )

# 第一层池化 (亚采样)
pool1 = tf.layers.max_pooling2d(
            inputs=conv1,
            pool_size=[2,2],
            strides=2,
            )

# 第二层卷积
conv2 = tf.layers.conv2d(
            inputs = pool1,
            filters = 64,
            kernel_size = [5,5],
            strides = 1,
            padding = "same",
            activation=tf.nn.relu
            )

# 第二层池化 (亚采样)
pool2 = tf.layers.max_pooling2d(
            inputs=conv2,
            pool_size=[2,2],
            strides=2,
            )

# 平坦化(flat)
flat = tf.reshape(pool2, [-1, 7*7*64])

# 神经元的全连接层
dense = tf.layers.dense(
            inputs = flat,
            units = 1024,
            activation = tf.nn.relu
            )

# Dropout(丢弃) tate=0.5
dropout = tf.layers.dropout(
              inputs = dense,
              rate = 0.5
              )

# 10个神经元的全连接层,这里不用激活函数来做非线性化了
logits = tf.layers.dense(
             inputs = dropout,
             units = 10)

# 计算误差(计算 cross entropy(交叉熵)), 再用softmax计算百分比概率)
loss = tf.losses.softmax_cross_entropy(onehot_labels=output_y, logits = logits)

# Adam 优化器最小化误差, 学习率 0.001
train_op = tf.train.AdamOptimizer(learning_rate = 0.001).minimize(loss)

# 精度. 计算预测值和实际标签的匹配程度
# 返回(accuracy, update_op), 只要第二个
accuracy = tf.metrics.accuracy(
                labels = tf.argmax(output_y, axis=1),
                predictions = tf.argmax(logits, axis=1)
                )[1]

#创建会话
sess = tf.Session()
#初始化变量: 全局和局部
init = tf.group(tf.global_variables_initializer(), tf.local_variables_initializer())
sess.run(init)

#训练神经网络
for i in range(100):
    batch = mnist.train.next_batch(50)
    train_loss, train_op_ = sess.run([loss, train_op], {input_x:batch[0], output_y: batch[1]})
    if i%100 == 0:
        test_accuracy = sess.run(accuracy, {input_x: test_x, output_y: test_y})
        print("Step=%d, Train loss=%.4f, [Test accuracy=%.2f]" % (i, train_loss, test_accuracy))

test_output = sess.run(logits, {input_x: test_x[:20]})
inference_y = np.argmax(test_output, 1)
print(inference_y, 'Inference numbers')
print(np.argmax(test_y[:20], 1), "Real numbers")

sess.close()