#！/usr/bin/env python3
# -*- coding:utf-8 -*-

'''打印如下图形
*
**
***
****
*****
'''
for i in range(5):
    print('*'*(i+1))


print('\nfromat使用\n')
print("{}: 计算机{}的CPU占用率为{}%。".format("2017-07-20","PYTHON",10))
print("{1}: 计算机{0}的CPU占用率为{2}%。".format("2017-07-20","PYTHON",10))

# print("{0:b},{0:c},{0:d},{0:o},{0:x},{0:X}".format(17))
print("{{0:b}}={0:b},{{0:c}}={0:c},{{0:d}}={0:d},{{0:o}}={0:o},{{0:x}}={0:x},{{0:X}}={0:X}".format(17))

print("{0:e},{0:E},{0:f},{0:%}".format(3.14))
print("{{0:e}}={0:e},{{0:E}}={0:E},{{0:f}}={0:f},{{0:%}}={0:%}".format(3.14))