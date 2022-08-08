#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 20:16
# @Author  : 羊驼
# @File    : mall.py
# @Software: PyCharm

from flask import Blueprint

mall_app = Blueprint("mall_app",__name__)

@mall_app.route("/mall")
def mall():
    return 'mall'

@mall_app.route("/aaa")
def aaa():
    return 'mall'
