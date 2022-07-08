#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/30 21:39
# @Author  : 羊驼
# @File    : mall.py
# @Software: PyCharm
from good import app



@app.route("/mall")
def mall():
    return "mall"


@app.route("/go")
def go():
    return "mall"