#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 21:22
# @Author  : 羊驼
# @File    : api2.py
# @Software: PyCharm\

from flask import Blueprint

api_app = Blueprint("api_app",__name__)

@api_app.route("/api2")
def api2():
    return "ok"
