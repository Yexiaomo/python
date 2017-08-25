#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 输入N个值计算平均值(哨兵循环-->以空格结尾结束输入)

def main():
    sum = 0.0
    cnt = 0
    xStr = input('Enter a number (<Enter to quit)>> ')
    while xStr != "":
        x = eval(xStr)
        sum += x
        cnt = cnt + 1
        xStr = input('Enter a number (<Enter to quit)>> ')
    print('\nThe average of the numbers is', sum/cnt)
main()