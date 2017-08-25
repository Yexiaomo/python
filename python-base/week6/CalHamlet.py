#!/usr/bin/env python3
# -*- coding:utf-8 -*-

### 词频统计之《哈姆雷特》
def getText():
    txt = open("hamlet.txt", 'r').read()
    txt = txt.lower()#所有单词转换为小写

    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':#将特殊字符转换为空格
        txt = txt.replace(ch,' ')
    return txt

hamletTxt = getText()
words = hamletTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<20}{1:>5}".format(word,count))