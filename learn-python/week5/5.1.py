#/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
给出三个点的坐标
若这三个点可以构成三角形，则输出三角形的周长
'''
import math

def square(x):
    return x*x

def distance(x1, y1, x2, y2):
    dist = math.sqrt( square(x1-x2) + square(y1-y2))
    return dist

def isTriangle(x1, y1, x2, y2, x3, y3):
    falg = ((x1-x2)*(y3-y2) - (x3-x2)*(y1-y2)) != 0
    return falg;

def main():
    print('Please enter (x,y) of three points in turn: ')
    x1, y1 = eval(input('Point1: (x, y) = '))
    x2, y2 = eval(input('Point2: (x, y) = '))
    x3, y3 = eval(input('Point3: (x, y) = '))

    # 判断是否可构成三角形
    if (isTriangle(x1,y1,x2,y2,x3,y3)):
        perim = distance(x1, y1, x2, y2) + distance(x1, y1, x3, y3) + distance(x2, y2, x3, y3)
        print('the perimeter of the triangle is: {0:.2f}'.format(perim))
    else:
        print('Are kidding me? this is not a troangle!!')


main()