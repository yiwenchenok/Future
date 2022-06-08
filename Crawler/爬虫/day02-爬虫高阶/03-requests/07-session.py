#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 07-session.py

import requests
#创建一个会话，可以保存cookie信息
sess = requests.session()  #urllib.request.HTTPCookieProcessor(cookie)

url = 'http://httpbin.org/cookies/set/name/yangtuo'
#利用session对象访问，会保存cookie
response = sess.get(url)

#是否能返回上一次的cookie信息
url2 = ''
url = 'http://httpbin.org/get'
res2 = sess.get(url).text
print(res2)