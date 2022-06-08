#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 01-urllib的高级使用.py

import urllib.request

"""
opener是 urllib.request.OpenerDirector 的实例，我们之前一直都在使用的urlopen，它是一个特殊的
opener（也就是模块帮我们构建好的）。
"""

#自定义http handdler处理器 处理http请求
http_handler = urllib.request.HTTPHandler(debuglevel=1)
https_handler = urllib.request.HTTPSHandler()

#自定义opener处理器
opner = urllib.request.build_opener(https_handler,https_handler)

# resp = urllib.request.urlopen('https://www.baidu.com')
resp = opner.open('https://www.baidu.com')
print(resp.status)
print(resp.read())