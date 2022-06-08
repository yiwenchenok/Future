#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 03-requests.py

import requests  # HTTP for Humans
data = requests.get('http://zb.yfb.qianlima.com/yfbsemsite/mesinfo/zbpglist?source=baidu3&e_matchtype=2&e_creative=46405068680&e_keywordid=225232036703&renqun_youhua=2587244&bd_vid=10273449485685086486')
print(data.status_code) #状态码，200表示成功 300 重定向 500服务器错付 404 网页不存在
print(data.apparent_encoding)  #获取网站的编码方式
# print(data.content) #获取bytes类型的网页源代码
print(data.text) #获取str类型的网页源代码

