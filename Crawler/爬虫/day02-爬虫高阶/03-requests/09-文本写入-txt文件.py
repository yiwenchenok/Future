#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 09-文本读取-txt文件.py
import requests

resp = requests.get("https://www.12306.cn/index/",verify=False) #访问https网站如果证书错误会报异常，可以设置不检查证书：virify=False

html = resp.text

with open('12306.txt','w',encoding='utf-8') as f:
    f.write(html)