#!/usr/bin/env python3
# -*- coding:utf-8 -*-

## matplotlib库


### 1.绘制散点图
# import matplotlib.pyplot as plt
# plt.plot([1, 2, 3, 4, 5, 6], 'ro')
# plt.ylabel('Description of y value')
# plt.show()

### 2.
# 利用 numpy库的linspace函数生成一个numpy数组X,包含了从-π到+π等间隔的256个值
# S和C则分别是这256个值对应的 其正弦x 和 其平方的余弦xian值组成numpy数组
# 再利用 plot函数打印相应图形
# import numpy as np
# from matplotlib.pyplot import *
# X = np.linspace( -np.pi, np.pi, 256, endpoint=True)
# C, S = np.cos(X*X), np.sin(X)
# plot(X, C, 'ro', label="$sin(x)$")
# plot(X, S, label="$cos(x^2)$")
# xlabel('xlabel')
# ylabel('ylabel')
# legend()
# title('This is Title')
# show()

'''
### 3.多子图绘制
# plot 子库也可以被用来生成多个子图
- 使用subplot()绘制含有多个子图的图表,语法如下
    subplot(nRows, mCols, plotNum)
- 图表的整个绘图区域被等分为n行m列,然后按照从左到右,从上到下的顺序对每个区域进行编号.左上区域的编号为 1
- ployNum参数指定所创建的子图编号
- 如果新创建的子图和之前创建的子图区域有重叠的部分,则之前的子图被覆盖
from matplotlib.pyplot import *
subplot(221)
subplot(222)
subplot(223)
subplot(224)
show()
'''

### 4.双子图绘制
# import numpy as np
# import matplotlib.pyplot as plt
# def f(t):
#     return np.exp(-t) * np.cos(2 * np.pi * t)
# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)
# plt.subplot(211)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
# plt.subplot(212)
# plt.plot(t2, np.cos(2* np.pi * t2), 'r--')
# plt.show()

### 5.直方图绘制
'''
# matplotlib提供的直方图绘制函数为 hist()
其中参数50表示直方图中直条即bin的个数
normed参数是一个布尔值,为真时,表示需要将直方图归一化
纵轴以概率的形式表示
text函数用来在指定位置添加文本标识
'''
# import numpy as np
# import matplotlib.pyplot as plt
# mu, sigma = 100, 15
# x = mu + sigma * np.random.randn(10000)
# plt.hist(x, 50, normed=1, facecolor='g')
# plt.xlabel('Smarts')
# plt.ylabel('Probability')
# plt.xlabel('Smarts')
# plt.title('Histogram of IQ')
# plt.text(60, 0.025, r'$\mu=100, \ \sigma=15$')
# plt.axis([40, 160, 0, 0.03])
# plt.show()


### 6.image子库
# image子库可对图像进行操作
# 如下, image子库的 imread函数将png图片各像素点的RGB值存入到numpy的数组中
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
img = mpimg.imread('.\\test.png')
plt.imshow(img)
plt.show()