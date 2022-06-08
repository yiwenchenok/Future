#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 11-json.dump.py
# json_dump.py

import json

listStr = [{"city": "北京"}, {"name": "张三"}]
with open('liststr.json','w',encoding='utf-8-sig') as f:
    json.dump(listStr,f,ensure_ascii=False)

dictStr = {"city": "北京", "name": "张三"}
with open('dictstr.json','w',encoding='utf-8-sig') as f:
    json.dump(dictStr,f, ensure_ascii=False)