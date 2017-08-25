#/usr/bin/env python3
# -*- utf-8 -*-

# 布尔运算符的使用
'''
这里列举or运算符的使用
什么都不输入默认值为vanilla
'''

def main():
   flavor = input('What flavor do you want [vanilla]:') or 'vanilla'
   print("flavor=%s" % flavor)

main()