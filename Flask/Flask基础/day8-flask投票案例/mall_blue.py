#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/30 21:39
# @Author  : 羊驼
# @File    : mall.py
# @Software: PyCharm
from flask import Blueprint

app_mall = Blueprint("app_mall",__name__)


@app_mall.route("/mall")
def mall():
    return "mall"


@app_mall.route("/go")
def go():
    return "mall"