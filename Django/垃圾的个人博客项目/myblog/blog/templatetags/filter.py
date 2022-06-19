#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : filter.py
from django import template
import re

register = template.Library()

@register.filter("my_filter")
def my_filter(value,num):
    """自定义truncatechars:xx"""
    num = int(num)
    reg = re.compile(r"<.*?>(.*?)<.*?>",re.S)
    text_list = reg.findall(value)
    st = ''.join([i.strip("\n") for i in text_list])
    return st[:num]

@register.filter("my_filter2")
def my_filter2(value,num):
    """自定义truncatechars:xx"""
    num = int(num)
    new_value = re.sub("[^\u4e00-\u9fa5，。？：“”；！]","",value)[:num]
    return new_value

