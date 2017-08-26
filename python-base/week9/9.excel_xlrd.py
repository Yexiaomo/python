#!/usr/bin/env python3
# -*- coding:utf-8 -*-
## xlrt库
# 打开excel文档
# workbook = xlrd.open_workbook('testread.xls')

# 获取所有sheet
# sheet_name = workbook.sheet_names() #返回类型为sheet名字组成list

## 获取指定sheet
# 根据sheet的sheet_by_index属性索引获取
# 根据sheet的sheet_by_name属性索引获取

## 利用xlrd模块读取并简单操作excel文档
# 获取指定sheet的名字,行数,列数, 调用指定sheet的name, nrows, ncols属性

## 获取sheet的内容
#  将sheet按照二维数组,根据行列的方式访问指定内容
#e.g. 第0行第1列数据 sheet.row(0)[1].value
#     第1行第0行数据 sheet.col(1)[0].value
#     第0行第1列数据 sheet.cell(0)[1].value

import xlrd

path = input("请输入excel文件路径:")
workbook = xlrd.open_workbook(path)
sheet = workbook.sheet_by_index(0)
print('-------------文件内容 Begin-------------')

for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        print("%s" % sheet.row(row)[col].value, '\t', end='')
    print()

print('-------------文件内容 End  -------------')