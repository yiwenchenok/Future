#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 06-requests设置代理.py
import requests
import random

#构建代理池
"""
123.171.42.75	3256	高匿名	HTTP	中国 山东 聊城 电信	1秒	2021-08-12 20:31:01
113.123.0.230	3256	高匿名	HTTP	中国 山东 威海 电信	0.6秒	2021-08-12 19:31:01
111.72.25.180	3256	高匿名	HTTP	中国 江西 抚州 电信	0.7秒	2021-08-12 18:31:01
60.168.81.247	1133	高匿名	HTTP	中国 安徽 合肥 电信	3秒	2021-08-12 17:31:01
"""
# proxy_list = ['202.55.5.209:8090']
# host_port = random.choice(proxy_list)
# # print(host_port)
# proxy_ip = {'http':f'http:{host_port}'}
url = 'https://www.baidu.com/s?wd=ip'
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
res = requests.get(url=url,headers=headers,proxies={"https":'114.199.69.4:3128'},timeout=10) #proxies设置代理
print(res.status_code)
# page_text=res.text
# with open("ip.html",'w',encoding='utf-8') as fp:
#     fp.write(page_text)

#加密代理
#todo:伪代码
# proxy_ip = {"http":'user:pass@118.156.78.90:8000'}
# res = requests.get(url,proxies=proxy_ip)  #proxies设置代理


