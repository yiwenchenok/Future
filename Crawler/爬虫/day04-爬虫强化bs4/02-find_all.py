#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 01-beatifulsoup.py

#安装bs4
#pip install beautifulsoup4

from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story1">Once upon a time there were three little sisters; and 
their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
and
<a href="http://example.com/tillie" class="sister2" id="link3">Tillie</
a>;
and they lived at the bottom of a well.</p>
<p class="story2">...</p>
'''

soup = BeautifulSoup(html,"lxml")

print(soup.find("a"))  #获取a标签,返回第一个
print(soup.a)  #这种方式只能获取到第一个标签

print("我是分割符".center(50,"*"))

print(soup.find_all("a"))  #获取a标签,返回列表，全文档匹配
print(soup.find_all("a",attrs={'class':"sister"}))  #获取a标签并且class为sister,返回列表，全文档匹配
