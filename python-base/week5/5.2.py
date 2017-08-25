#/usr/bin/env python3
# -*- coding: utf-8 -*-

def change(l):
    print('函数内部修改前:', l)
    for i in range(len(l)):
        l[i] = l[i] + i
    print('函数内部修改后:', l)

def main():
    test = [1,2,3]
    print('执行函数前:', test)
    change(test)
    print('执行函数后:', test)

main()
'''
以上程序可知
 1.python的参数是通过值来传递的
 2.如果变量是可变对象（如列表、图形队形等）返回到调用程序时该对象会呈现被修改后的状态
 而旧值（test中的值）在 python垃圾数据回收的时候被清理掉
'''