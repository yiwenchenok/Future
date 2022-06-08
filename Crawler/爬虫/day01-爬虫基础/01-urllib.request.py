#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 01-urllib.request.py

from urllib import request

data = request.urlopen("http://www.baidu.com")
# print(data.status) #响应码  200表示成功 300表示重定向 500服务器错误  400没有权限
# print(data.getheader("Content-Type")) #获取相应头指定名字的值
# print(data.getheader("Set-Cookie"))
# print(data.readline()) #获取相应对象的一条数据
# print(data.info()) #获取相应对象所有header信息
# print(data.read().decode())  #todo:读取响应对象的源代码