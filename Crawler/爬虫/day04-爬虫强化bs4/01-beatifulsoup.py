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
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</
a>;
and they lived at the bottom of a well.</p>
<p class="story2">...</p>
'''

soup = BeautifulSoup(html,"lxml")
print(type(soup)) #<class 'bs4.BeautifulSoup'>
print(soup.title)  #soup.标签名称，获取到对应标签
print(soup.title.string)  #string 获取标签文本
print(soup.title.get_text())  #string 获取标签文本
print(soup.a)  #这种方式只能获取到第一个标签
print(soup.a["id"]) #获取a标签的id属性  可以省略.attrs
print(soup.a["href"]) #获取a标签的href属性

print(soup.a.attrs) #获取标签a的所有属性值，返回一个字典
print(soup.a.attrs["id"]) #获取a标签的id属性
print(soup.a.attrs["href"]) #获取a标签的href属性

print("我是分隔符".center(50,"*"))
print(soup.body.contents)  #获取body标签的所有子孙节点
print(soup.p.children)  #获取p标签下的子节点，返回迭代器
for i in soup.p.children:
    print(i)

print(soup.find("p",attrs={'class':"story2"}))  #获取p标签并且class为story2
print(soup.find("a",attrs={'id':"link1"}))  #获取a标签并且id为link1


print(soup.find("a"))  #获取a标签,返回第一个
print(soup.a)  #这种方式只能获取到第一个标签


