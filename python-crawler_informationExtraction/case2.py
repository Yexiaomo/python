#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
亚马逊商品页面简单爬取, 任意商品
'''
import requests

def getHTMLText():
    try:
        # 这仅仅是因为utf-8编码,不必理会原为(https://www.amazon.cn/图书/dp/B00GHGZLWS)
        url = 'https://www.amazon.cn/%E5%9B%BE%E4%B9%A6/dp/B00GHGZLWS'
        kv = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv, timeout=30)
        r.status_code
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "发生异常,爬取失败"

def main():
    htmlText = getHTMLText()
    index = htmlText.index("利用Python进行数据分析")
    print(htmlText[index-200:index+500])

if __name__ == '__main__':
    main()