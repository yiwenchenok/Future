#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 05-requests发送post请求.py
import requests
#构造请求地址
url = 'http://httpbin.org/post'
#构造form_data
form_data = {'query': 'dog'}
#构造请求头
header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
}

resp = requests.post(url,headers=header,data=form_data,timeout=3)
# print(resp.text)
print(resp.status_code)

print(resp.json())  #如果返回的是字典类型，我们直接将其转成字典
print(type(resp.json()))
