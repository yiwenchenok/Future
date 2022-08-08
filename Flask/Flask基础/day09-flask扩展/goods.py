#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 20:16
# @Author  : 羊驼
# @File    : goods.py
# @Software: PyCharm

from flask import Flask,render_template
from app.mall import mall_app
from app.cart import cart_app
from app2.user import user_app
app = Flask(__name__)
app.register_blueprint(mall_app)
app.register_blueprint(cart_app)
app.register_blueprint(user_app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/user")
def user():
    return 'goods'

@app.route("/order")
def order():
    return 'goods'

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
