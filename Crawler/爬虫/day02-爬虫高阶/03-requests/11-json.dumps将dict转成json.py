#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 11-json.dumps将dict转成json.py
# json_dumps.py

import json
import chardet

listStr = [1, 2, 3, 4]
tupleStr = (1, 2, 3, 4)
dictStr = {'city': '北京', 'name': '张三'}

json.dumps(listStr)
# '[1, 2, 3, 4]'
json.dumps(tupleStr)
# '[1, 2, 3, 4]'

# 注意：json.dumps() 序列化时默认使用的ascii编码
# 添加参数 ensure_ascii=False 禁用ascii编码，按utf-8编码
# chardet.detect()返回字典, 其中confidence是检测精确度

json.dumps(dictStr)
# '{"city": "\\u5317\\u4eac", "name": "\\u5f20\\u4e09"}' #json数据自动按Unicode存储


print(json.dumps(dictStr, ensure_ascii=False))
# {"city": "北京", "name": "张三"}
print(type(json.dumps(dictStr, ensure_ascii=False))) #<class 'str'>