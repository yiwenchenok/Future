#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 20:26
# @Author  : 羊驼
# @File    : user.py
# @Software: PyCharm
from flask import Blueprint

user_app = Blueprint("user_app",__name__)

@user_app.route("/uuuu")
def uuuu():
    return "ok"