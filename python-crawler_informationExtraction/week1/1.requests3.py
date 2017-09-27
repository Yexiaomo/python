#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
#### requests.request(method, url, **kwargs)
- method:请求方式,对应get/put/post等7种
- url:拟获取页面的url链接

**kwargs:控制访问参数,13个,下面详细介绍
- params:字典或字节序列,作为参数增加到url中

- data:字典,字节序列或文件对象,作为request的内容
- json: JSON格式数据,作为request的内容
- headers: 字典,HTTP定制头
- cookies: 字典或Cookiejar,request中的cookie
- auth: 元组,支持HTTP认证功能
- files: 字典类型,传输文件
    >>>fs = {'file': open('data.xls', 'rb')}
    >>>r = requests.request('POST','http://fanxiaobo.cn',files=fs)
- timeout:设定超时时间,单位秒
- proxies: 字典类型,设定访问代理服务器,可以增加登录认证
pxs = {'http':'http://user:pass@10.10.10.1:1234'
       'https':'https://user:10.10.10.1:4321'}
r = requests.request('GET','http://www.baidu.com', proxies=pxs)

- allow_redirects: True/False, 默认为True,重定向开关
- stream: True/False,默认为 True, 获取内容立即下载开关
- verify: True/False,默认为True,认证SSL证书开关
- cert: 本地SSl证书路径