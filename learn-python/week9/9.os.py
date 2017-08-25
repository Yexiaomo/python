#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''python
### os库->python安装后自带的函数库,处理操作系统相关功能
os.getcwd() 获得当前工作目录
os.listdir(path) 返回指定目录下的所有文件和目录名
os.remove() 删除一个文件
os.removedirs(path) 删除多个目录
os.chdir(path) 更改当前目录到指定目录

os.mkdir(path) 新建一个目录
os.rmdir(name) 删除一个目录
os.rename(src, dst) 更改文件名

os.path 处理操作系统目录的字库
os.path.isfile() 检验路径是否是一个文件
os.path.isdir() 检验路径是否是一个目录
os.path.exists() 检验路径是否存在
os.path.split() 返回一个路径的目录名和文件名
os.path.splitext() 分离扩展名
os.path.dirname 获得路径名
os.path.basename() 获得文件名
os.path.getsize() 获得文件大小
os.path.join(path, name) 返回绝对路径

os.walk(path) 用于遍历一个目录, 返回一个三元组
root, dirs, files = os.walk(path) #root 是字符串, dirs和files 是列表类型, 表示root中所有的目录和所有文件
'''

#### 将输入路径下的所有文件名字后添加一个字符串 "_py"
# 轻易不要尝试
# import os
# path = input("输入一个路径:")
# for root, dirs, files in os.walk(path):
#     for name in files:
#         fname, fext = os.path.splitext(name)
#         os.rename(os.path.join(root, name), os.path.join(root, fname+'_py'+fext))