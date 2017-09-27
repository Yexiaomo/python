#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
## ip地址归属地查询
查询工具: ip.cn
查询地址[http://www.ip.cn/index.php]
所查询 IP: 123.206.124.144 为例
'''
import requests
try:
    kw = {'ip':'123.206.124.144'}
    url = 'http://www.ip.cn/index.php'
    r = requests.get(url, params=kw)
    r.encoding = r.apparent_encoding
    r.url
    index = r.text.index('id="result"')
    print(r.text[(index-5):(index+220)])
except:
    print('爬取失败')