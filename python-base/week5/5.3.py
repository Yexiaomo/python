#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''python
 1. 求阶乘
 2. 反转字符串
'''
def fact(n):
    if n==0 :
        return 1
    else:
        return n * fact(n-1)

def reverse(s):
    if s == "":
        return s
    else:
        return reverse(s[1:]) + s[0]
        
def main():
    n = int(input('Please enter a int type number n = '))
    print('{}! = {}\n'.format(n,fact(n)))
    s = input('Please any letters: ')
    print('reverse(s) =', reverse(s))

main()