#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# 文件基本操作
'''
### 文件打开
    <variable> = open(<name>, <mode>)
name:磁盘文件名
mode:打开模式，有以下几种
- r: 只读. 如果文件不存在,则输出错误
- w: 只写. 如果文件不存在,则自动创建文件
- a: 表示附加到文件末尾
- rb: 只读二进制文件. 如果文件不存在,则输出错误
- wb: 只写二进制文件. 如果文件不存在,则自动创建文件
- ab: 附加到二进制文件末尾
- r+: 读写

### 文件读取
- read() 返回值为包含整个文件内容的一个字符串
- readline() 返回值为文件下一行内容的字符串
- readlines() 返回值为整个文件内容的列表,每项是以换行符为结尾的一行字符串

### 写入文件
- 从计算机内存向文件写入数据
- write() 把含有文本数据或二进制数据块的字符串写入文件中
- writelines() 针对列表操作, 接收一个字符串列表作为参数,将它们写入文件

'''

def main():
    # fname = input('Please enter filename: ')
    # infile = open(fname,'r')

    # 1.1 OutPut file content
    # data = infile.read()
    # print('file content is:',data)

    # 1.2 OutPut the first 5 lines of content
    # for i in range(5):
    #     dl = infile.readline()
    #     print(dl[:-1])

    # 2.1 Write content
    # outfile = open("outfile.txt", 'w')
    # outfile.writelines(['Hello',' ','World','!'])
    # outfile.close()
    # _infile = open('outfile.txt', 'r')
    # print(_infile.read())

    # 2.2 Traversal file
    # e.g.1
    '''python
        file = open(somefile, 'r')
        for line in file.readlines():
            operation 
    '''
    # e.g.2
    '''python
        file = open(somefile, 'r')
        for line in file:
            operation
    '''
main()