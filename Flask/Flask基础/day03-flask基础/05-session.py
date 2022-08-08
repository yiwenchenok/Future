#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : 羊驼
# @email  : 249084156@qq.com
# @File desc  : 05-session.py
from flask import Flask,session
from datetime import datetime,timedelta

app = Flask(__name__)

app.config["SECRET_KEY"] ="kladjkljgkalj&&i89889%%jkjkkfklsgj"

@app.route('/set_session')
def set_session():
    """设置session"""
    session["name"] = "yangtuo"
    session["id"] = "0000"

    session.permanent =  True #开启session超时
    app.permanent_session_lifetime = timedelta(seconds=10) #10秒过期


    return 'ok'


@app.route('/get_session')
def get_session():
    """获取session"""



    name = session.get("name")
    id = session.get("id")

    return f"name:{name},id:{id}"


@app.route("/del_session")
def del_session():
    # name = session.pop('name')  #删除并且返回这个name
    # return f"删除session:{name}"
    session.clear() #清空所有的session信息

    return "ok"



if __name__ == '__main__':
    app.run(debug=True)
