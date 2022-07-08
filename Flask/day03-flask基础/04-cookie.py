#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : 羊驼
# @email  : 249084156@qq.com
# @File desc  : 04-cookie.py
from flask import Flask,make_response,request
from datetime import datetime

app = Flask(__name__)


@app.route('/set_cookie')
def set_cookie():
    """设置cookie"""
    response = make_response("写入cookie")

    response.set_cookie('name',"yangtuo",max_age=5) #超时时间5秒
    response.set_cookie('name2',"python",expires=datetime(2022,2,10))
    return response

@app.route("/get_cookie")
def get_cookie():
    """获取cookie"""
    cookie = request.cookies #获取所有的cookie信息
    name = cookie.get("name")
    name2 = cookie.get("name2")

    return f"name:{name},name2:{name2}"

@app.route("/del_cookie")
def del_cookie():
    response = make_response("删除cookie")
    response.delete_cookie('name2') #删除key为name2的cookie
    return response


if __name__ == '__main__':
    app.run(debug=True)
