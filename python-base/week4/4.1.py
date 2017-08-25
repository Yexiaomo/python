#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 寻找一组数中最大值

def main():
    n = eval(input('How many numbers are there:'))
    max = eval(input('Enter a number:'))
    for i in range(n-1):
        x = eval(input('Enter a number:'))
        if x>max:
            max = x
        print('The largest number is', max,'\n')

main()

# 或者使用内置函数
print('/n******  fun 函数 ******/n')
def fun():
    x1,x2,x3=eval(input('Please enter three values:'))
    print('The largest number is',max(x1,x2,x3))
fun()