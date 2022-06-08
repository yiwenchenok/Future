#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 10-json用法.py
# json_loads.py

import json

strList = '[1, 2, 3, 4]'

strDict = '{"city": "北京", "name": "张三"}'

print(json.loads(strList))
print(type(json.loads(strList)))  #<class 'list'>
# [1, 2, 3, 4]

print(json.loads(strDict))
# {'city': '北京', 'name': '张三'}
print(type(json.loads(strDict)))  #<class 'dict'>


