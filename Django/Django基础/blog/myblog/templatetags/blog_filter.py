#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : blog_filter.py

from django import template

#1.实例化注册器
register = template.Library()
# @register.filter  #过滤器名称使用函数名称
@register.filter("mod")  #mod过滤器名称
def mod(value,num):  #2.定义过滤器函数
    """
    实现过滤器，判断是否被num整除
    :param value: 模板中的变量
    :param num: 开发人员所传的参数
    :return: 过滤器处理之后的结果，必须返回
    """
    return value % int(num)
# register.filter("mod",mod)  #3.注册过滤器，第一个是过滤器的名称
@register.filter("modTwo")  #mod过滤器名称
def modTwo(value):
    """
    实现过滤器，判断是否被2整除
    :param value: 模板中的变量
    :return: 过滤器处理之后的结果，必须返回
    """
    return value % 2
