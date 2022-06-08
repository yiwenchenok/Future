#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 01-urllib.request.py

from urllib import request

data = request.urlopen("http://www.baidu.com")

# print(data.read().decode())  #todo:读取响应对象的源代码
with open('baidu.html','wb') as f:
    f.write(data.read())