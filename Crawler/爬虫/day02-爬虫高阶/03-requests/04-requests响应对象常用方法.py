#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 04-requests响应对象常用方法.py

import requests

# url = 'http://httpbin.org/get'
url = 'http://www.baidu.com/'
resp = requests.get(url)
# print(resp.text.encode('utf-8'))
# print(resp.content)
resp.encoding = resp.apparent_encoding  #处理编码的方式，通过返回的代码自己判断编码格式
print(resp.cookies) #获取cookie

# print(resp.headers)  #获取头部信息
# print(resp.iter_content())  #返回一个元素是网站源码的迭代器
#
# print(resp.reason) #错误信息： ok表示没有错误 Not Found 404
# print(resp.links) #