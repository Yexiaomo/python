#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
## 网络图片的简单爬取和存储
图片来源国家地理[http://www.nationalgeographic.com.cn]
图片地址[http://image.nationalgeographic.com.cn/2017/0825/20170825023807131.jpg]
'''
'''python
# 参考代码1
# import requests
# def getHTMLText(url):
#     try:
#         r = requests.get(url)
#         r.status_code
#         r.encoding = r.apparent_encoding
#         return r.content
#     except:
#         return '爬取失败,发生异常'

# def main():
#     path = "./case4.jpg"
#     imgUrl = input('Please enter image[type=jpg] link:')
#     imgFile = open(path, 'wb')
#     imgFile.write(getHTMLText(imgUrl))
#     imgFile.close()

# if __name__ == '__main__':
#     main()
'''
# 参考代码2
import requests
import os
imgUrl = "http://image.nationalgeographic.com.cn/2017/0825/20170825023807131.jpg"
fileRoot = "E://picture//"
imgPath = fileRoot + imgUrl.split('/')[-1]
try:
    if not os.path.exists(fileRoot):
        os.mkdir(fileRoot)
    if not os.path.exists(imgPath):
        r = requests.get(imgUrl)
        r.status_code
        with open(imgPath, 'wb') as imgFile:
            imgFile.write(r.content)
            imgFile.close()
            print('图片保存成功')
    else:
            print('文件已存在')
except:
    print('爬取失败')