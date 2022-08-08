#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 20:25
# @Author  : 羊驼
# @File    : cart.py
# @Software: PyCharm

from flask import Blueprint

cart_app = Blueprint("cart_app",__name__)

@cart_app.route("/cccc")
def cccc():
    return 'cccc'


