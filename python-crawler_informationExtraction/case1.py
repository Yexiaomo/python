#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
京东商品页面简单爬取, 任意商品
'''
import requests

def getHTMLText():
    try:
        url = 'https://item.jd.com/11352441.html'
        r = requests.get(url, timeout=30)
        r.status_code
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "发生异常,爬取失败"

def main():
    htmlText = getHTMLText()
    print(htmlText[:1000])

if __name__ == '__main__':
    main()