#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
实现百度或360搜索关键词提交
- 百度关键词接口
http://www.baidu.com/s?wd=keyword
- 360关键词接口
http://www.so.com/s?q=keyword
'''
## 以搜索 python 为例
import requests

def getHTMLText(url):
    try:
        if 'baidu' in url:
            kw = {'wd':'python'}
        else:
            kw = {'q':'python'}

        r = requests.get(url, params=kw)
        r.status_code
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '爬取失败,发生异常'

def main():
    bdUrl = 'http://www.baidu.com/s'
    soUrl = 'http://www.so.com/s'
    bdHtmlText = getHTMLText(bdUrl)
    soHtmlText = getHTMLText(soUrl)
    print('百度搜索返回的字符串长度',len(bdHtmlText))
    print('360搜索返回的字符串长度',len(bdHtmlText))

if __name__ == '__main__':
    main()