#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : 羊驼
# @email  : 249084156@qq.com
# @File desc  : 02-重定向.py
from flask import Flask,make_response,render_template,jsonify
app = Flask(__name__)


# @app.route("/")
# def index():
#     # return ("index","888 yangtuo",{"Content-Type": "image/jpeg"})
#
#     with open("templates/index.html",'r',encoding='utf-8')  as f:
#         htm = f.read()
#     response = make_response(htm,8888)
#     response.headers["Content-Type"] = "text/html"
#     return response


@app.route("/")
def index():

    context = {
        "name":"yangtuo",
        "age":18
    }
    return render_template('index.html',**context) #*args **kwargs

@app.route("/index2")
def index2():
    js = [{'desc':{"name":"羊驼",'age':10},"tel":"1234567"}]
    return jsonify(js)  #返回一个json数据类型的响应


if __name__ == '__main__':
    app.run(debug=True)

