#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 20:57
# @Author  : 羊驼
# @File    : __init__.py.py
# @Software: PyCharm
from config import CONFIG
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql  #pip install pymysql



pymysql.install_as_MySQLdb()
db = SQLAlchemy()


def create_app(config="local"): #默认开发模式
    app = Flask(__name__)
    db.init_app(app)
    # 加载配置信息
    Config = CONFIG[config]
    app.config.from_object(Config)  #根据传参加载不同的配置

    # from movie.views.vote import vote, index #循环导入
    from movie.views.vote import vote_app
    app.register_blueprint(vote_app)

    from movie.views.api2 import api_app
    app.register_blueprint(api_app)

    return app


app = create_app(config="local") #默认开发模式 #flask实例
# app = create_app(config="product") #线上模式 #flask实例


@app.route("/index")
def aaa():
    return "ok"

