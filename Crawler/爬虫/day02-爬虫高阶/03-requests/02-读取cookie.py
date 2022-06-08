#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 02-读取cookie.py
import http.cookiejar
import urllib.request

#创建一个cookie保存对象
cookie = http.cookiejar.LWPCookieJar()

#读取cookie
cookie.load('cookie.text',ignore_discard=True,ignore_expires=True)
for i in cookie:
    print(i)


#创建一个handler
cookie_handle = urllib.request.HTTPCookieProcessor(cookie)
#自定义opener
opener = urllib.request.build_opener(cookie_handle)
opener.open("https://www.baidu.com")
