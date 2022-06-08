#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 01-re.py
import re

str_ = 'hellokk world hello world'
print(re.findall('hello',str_))
print(re.findall(r'hello\b',str_))

#中文
#[\u4e00-\u9fa5]
str_ = 'hellokk world 我是中文的字体hello world'
print(re.findall('[\u4e00-\u9fa5]{1,999}',str_,re.I))
#正则的split
str2='python12java34c++456python'
print(str2.split('12'))
print(re.split('\d{1,9}',str2))
#正则的sub替换
str3='java is good,java is better'
print(re.sub('java','python',str3,count=0))