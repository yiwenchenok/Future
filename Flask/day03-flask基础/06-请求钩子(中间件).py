#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : 羊驼
# @email  : 249084156@qq.com
# @File desc  : 06-请求钩子(中间件).py
# coding=utf-8
# 导入Flask类
from flask import Flask, abort
import datetime
# Flask 接收一个参数 name ,
# 导入模块的目录， flask以这个目录为基础，寻找静态文件目录static和模板目录templates
app = Flask(__name__)


# 只有在第一次请求的时候执行
@app.before_first_request
def first_request():
    """只有在第一次请求的时候执行"""
    print("before_first_request 执行")

# 每次请求之前执行
@app.before_request
def before_request_():
    """在执行视图函数之前执行"""
    print('before_request执行')

# 每次执行完成后没有未处理的异常抛出才会执行
@app.after_request
def after_request(response):
    """执行完视图函数，但没有异常情况下执行，要返回response"""
    print('after_request 执行')
    return response



@app.teardown_request
def teardown_request_(response):
    """执行完视图函数，不管有没有异常情况下都会执行，要返回response"""
    print('teardown_request 执行')
    return response

@app.route('/')
def index():
    print('index 执行')
    return 'ok'
if __name__ == '__main__':
    # Flask 应用程序实例的方法run启动web服务器
    app.run(debug=True)
