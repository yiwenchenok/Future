#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 03-认证代理（花钱买）.py

import urllib.request
import random



#todo:伪代码
proxy_ip = {"http":'user:pass@118.156.78.90:8000'}




#构造代理处理器
Proxy_handler = urllib.request.ProxyHandler(proxy_ip)

#自定义opener
opener = urllib.request.build_opener(Proxy_handler)

url = 'https://www.hao123.com'
resp = opener.open(url)
print(resp.read().decode())

