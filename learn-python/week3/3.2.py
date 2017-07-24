#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import random
import math
import time


'''
### 蒙特卡洛 求 圆周率
IPO 如下
- 输入： 抛点的数量
- 处理： 对于每个抛洒点，计算点到圆心的距离，
通过距离判断该点在圆内或圆外。统计在圆内点的数量
- 输出圆周率
'''
#pi.py

DARTS = 12000
hits = 0
time.clock()
for i in range(1, DARTS):
    x, y = random.random(), random.random()
    dist = math.sqrt(x**2 + y**2)
    if dist <= 1.0 :
        hits = hits+1
pi = 4*(hits/DARTS)
print('Pi 的值为： %s' % pi)
print('程序运行时间为： %-5.5s' % time.clock())