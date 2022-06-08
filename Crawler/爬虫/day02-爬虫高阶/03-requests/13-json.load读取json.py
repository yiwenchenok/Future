#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 13-json.load读取json.py
# json_load.py

import json

strList = json.load(open("liststr.json",encoding='utf-8-sig'))
print(strList)
print(type(strList))


strDict = json.load(open("dictstr.json",encoding='utf-8-sig'))
print(strDict)