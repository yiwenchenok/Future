#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : 羊驼
# @email  : 249084156@qq.com
# @File desc  : 02-重定向.py
from flask import Flask,abort,redirect,render_template
app = Flask(__name__)

@app.route('/login')
def login():
    login_ = True

    if login_ == True:
        return redirect("/index")
    else:
        return render_template('login.html')


@app.route("/index")
def index():
    return "index"


if __name__ == '__main__':
    app.run(debug=True)

