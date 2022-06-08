#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 03-获取请求参数.py

from urllib import request

response = request.urlopen("http://httpbin.org/get?name=yangtuo&age=18")
print(response.read().decode())