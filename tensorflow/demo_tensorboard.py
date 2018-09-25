# -*- coding: utf-8 -*-
# 引入需要的库
import tensorflow as tf

# 构造图的结构
# 用一个线性方程的例子 y = W * x + b
W = tf.Variable(2.0, dtype=tf.float32, name="Weight") #权重
b = tf.Variable(1.0, dtype=tf.float32, name="Bias") # 偏差
x = tf.placeholder(dtype=tf.float32, name="input") # 输入

with tf.name_scope("Output"): # 输出
    y = W * x + b

# 定义保存日志路径 (为了在tensorboard中打开)
path = "./log"

# 创建用于初始化所有变量(Variable)的操作
init = tf.global_variables_initializer()

# 创建会话 Session
with tf.Session() as sess:
    sess.run(init) # 初始化变量
    writer = tf.summary.FileWriter(path, sess.graph)
    result = sess.run(y, {x: 3.0})
    print("y = %s" % result) 
# 运行结束后创建的日志在log文件下
# 使用tensorboard命令打开, 格式如下
#
    tensorboard --logdir=日志文件夹名称
    这里就是使用
    tensorboard --logdir=log
#