#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
爬取某个链接100次所需要的时间
'''
import requests
import time

urlDic={}

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '产生异常'
def fun(url):
    startTime = time.clock()
    for i in range(1, 101):
        print(getHTMLText(url))
    endTime = time.clock()
    urlDic[url] = endTime - startTime

def main():
    while True:
        url=input("Please enter a link(End input enter '@'):")
        if url == "@":
            print('bye')
            break
        fun(url)
    for key, value in urlDic.items():
        print('爬取网站:{0} 100次需要的时间为{1:.2f}s'.format(key, value))

if __name__ == '__main__':
    main()