#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : 羊驼
# @email  : 249084156@qq.com
# @File desc  : 01-abort函数抛出异常.py
from flask import Flask,abort
app = Flask(__name__)
@app.route("/<flag>",methods=["get",'post'])
def index(flag):
    if flag == "del":
        abort(404)  #抛出404错误
    return f"ok:{flag}"

@app.errorhandler(404)
def error_404(e):
    """
    自定义错误视图，作用于全局，接收一个参数，自带的404错误视图返回的信息
    :param e:
    :return:
    """
    return f"你想干啥，我这边没有你想要的东西【404错误】"


if __name__ == '__main__':
    app.run(debug=True)






