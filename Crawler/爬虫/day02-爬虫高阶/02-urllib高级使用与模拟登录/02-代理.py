#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 02-代理.py
import urllib.request
import random

"""
106.45.104.249	3256	高匿名	HTTP	中国 宁夏 中卫 电信	0.4秒	2021-08-10 19:31:01
121.232.148.90	3256	高匿名	HTTP	中国 江苏 镇江 电信	0.7秒	2021-08-10 18:31:01
175.7.199.185	3256	高匿名	HTTP	中国 湖南 张家界 电信	0.6秒	2021-08-10 17:31:01


"""

#代理池： 键为协议，值为ip加端口
proxy_list = [
    {'http':'http://106.45.104.249:3256'},
    {'http':'http://121.232.148.90:3256'},
    {'http':'http://175.7.199.185:3256'},
]

#随机从ip列表中获取一个代理
proxy_ip = random.choice(proxy_list)

#构造代理处理器
Proxy_handler = urllib.request.ProxyHandler(proxy_ip)

#自定义opener
opener = urllib.request.build_opener(Proxy_handler)

url = 'https://www.hao123.com'
resp = opener.open(url)
print(resp.read().decode())

resp2 = urllib.request.urlopen(url)
print(resp2.read().decode())