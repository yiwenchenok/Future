#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/30 21:37
# @Author  : 羊驼
# @File    : good.py
# @Software: PyCharm

from flask import Flask
# from mall import mall  #循环导入
app = Flask(__name__)

#避免循环的解决方案：蓝图
from mall_blue import app_mall
app.register_blueprint(app_mall)


@app.route("/")
def index():
    return "index"

@app.route("/goods")
def goods():
    return "goods"

@app.route("/cart")
def cart():
    return "cart"


if __name__ == '__main__':
    print(app.url_map)
    app.run()
