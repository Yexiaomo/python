#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''问题描述
    生成一个test.txt文件包含 '中国是一个伟大的国家'
'''
s = '中国是一个伟大的国家'
s = s.encode('utf-8')
# outfile = open('test.txt', 'bw')
# outfile.write(s.encode('utf-8'))
outfile = open('test.txt', 'w')
outfile.write(s)
outfile.close()