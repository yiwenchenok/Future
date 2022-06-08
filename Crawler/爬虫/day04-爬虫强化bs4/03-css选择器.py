#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 03-css选择器.py
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
<p class="story2"><b>The Dormouse's story</b></p>
'''

soup = BeautifulSoup(html,"lxml")

print(soup.find_all("a",attrs={'class':"sister"}))  #获取a标签并且class为sister,返回列表，全文档匹配
print(soup.select('.sister'))  #获取所有class为sister的标签
print(soup.select(".title > b"))
print(soup.select(".story1 > .sister2"))

aaa = soup.select(".story1 > .sister2")[0]
print(aaa)
print(type(aaa))  #<class 'bs4.element.Tag'>
print(aaa["href"])
print(aaa.attrs["id"])
