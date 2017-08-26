#!/usr/bin/env python3
# -*- coding:utf-8 -*-
## xlwt库
##创建工作簿
# file = xlwt.Workbook() #调用xlwt的Workbook实现

## 创建sheet
# 调用add_sheet返回一个Worksheet类
# 创建sheet有可选参数cell_overwrite_ok, 表示是否可以覆盖单元格,默认为false

## sheet的内容添加,调用sheet的write属性实现
# 常用write用法: write(x, y, string, style) -->x:行 , y:列

import xlwt

testExcel = xlwt.Workbook('test.xls')
sheet = testExcel.add_sheet('sheet1')
for i in range(5):
    for j in range(3):
        s = "第"+str(i)+"行第"+str(j)+"列"
        sheet.write(i, j, s)

testExcel.save('test.xls')