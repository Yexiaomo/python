#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
### requests库常用方法
- requests.request() 构造一个请求, 支撑以下各种方法的基础方法
- requests.get()  获取HTML网页的主要方法, 对应于HTTP的GET
- requests.head() 获取HTML网页头信息,对应于HTTP的HEAD
- requests.post() 向HTML网页提交POST请求,对应于HTTP的POST
- requests.put()  向HTML网页提交PUT请求,对应于HTTP的PUT
- requests.patch() 获取HTML网页提交局部修改请求,对应于HTTP的PATCH
- requests.delete() 获取HTML网页提交删除请求,对应于HTTP的DELETE
'''
'''
### Response对象的属性
- r.status_code   HTTP请求的返回状态, 200表示连接成功, 404表示失败
- r.text          HTTP响应内容的字符串形式,即 url 对应的页面内容
- r.encoding      从HTTP header 中猜测的响应内容编码方式
- r.apparent_encoding 从内容中分析出的响应内容编码方式(备选编码方式)
- r.content       HTTP响应内容的二进制形式
'''

import requests
r=requests.get("http://www.baidu.com")
print(r.status_code) # 200
print(type(r)) # <class 'requests.models.Response'>
print(r.headers) # {'Pragma': 'no-cache', 'Date': 'Fri, 25 Aug 2017 14:42:25 GMT', 'Last-Modified': 'Mon, 23 Jan 2017 13:27:36 GMT', 'Server': 'bfe/1.0.8.18', 'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform', 'Content-Encoding': 'gzip', 'Set-Cookie': 'BDORZ=27315; max-age=86400; domain=.baidu.com; path=/', 'Content-Type': 'text/html', 'Connection': 'Keep-Alive', 'Transfer-Encoding': 'chunked'}
print(r.encoding) # 'ISO-8859-1'
print(r.apparent_encoding) # 'utf-8'
r.encoding = r.apparent_encoding
print(r.text)