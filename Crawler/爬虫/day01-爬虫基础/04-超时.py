#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 04-超时.py

from urllib import request

data = request.urlopen("http://www.baidu.com",timeout=0.001)  #设置请求超时时间:如果在指定时间内没有得到响应，则抛出异常
print(data.read().decode())