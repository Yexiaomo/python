# -*- coding:utf-8 -*-
'''
用梯度下降的优化方法来快速解决线性回归问题
'''

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 
#构建数据
points_num = 100
vectors = []
#用numpy的正态随机分布函数生成100个点
#用这些点(x,y)坐标值对应线性方程y=0.1*x + 0.2
#权重(Weight)0.1, 偏差(Bias) 0.2
for i in range(points_num):
    x1 = np.random.normal(0.0, 0.66)
    y1 = 0.1*x1 + 0.2 + np.random.normal(0.0, 0.04)
    vectors.append([x1, y1])

x_data = [v[0] for v in vectors] # 真实点的x坐标
y_data = [v[1] for v in vectors] # 真实点的y坐标

#图像1: 展示100个随机数据点
plt.plot(x_data, y_data, 'r*', label="Original data") #红色星形的点
plt.title("Linear Regression using Gradient Descent")
plt.show()

# 构建线性回归模型
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0)) #初始化Weight
b = tf.Variable(tf.zeros([1])) # 初始化Bias
y = W*x_data + b               # 模型计算出来的y

#定义loss function(损失函数) 或 cost function(代价函数)
# 对Tensor的所有维度计算 ((y-y_data)^2) / N
loss = tf.reduce_mean(tf.square(y-y_data))

# 用梯度下降优化器来优化loss function()
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# 创建会话
sess = tf.Session()
#初始化变量
init = tf.global_variables_initializer()
sess.run(init)

# 训练20步(数据量少)
for step in range(20):
    # 优化每一步
    sess.run(train)
    # 打印每一步的损失,权重和偏差
    print("Step=%d, Loss=%f, [Weight=%f Bias=%f]"  % (step, sess.run(loss), sess.run(W), sess.run(b)))

#图像2: 绘制所有的点并且绘制出最佳拟合的直线
plt.plot(x_data, y_data, 'r*', label="Original data") #红色星形的点
plt.title("Linear Regression using Gradient Descent")
plt.plot(x_data, sess.run(W) * x_data + sess.run(b), label="Fitted line") #拟合的线
plt.xlabel('x')
plt.ylabel('y')
plt.show()
sess.close()