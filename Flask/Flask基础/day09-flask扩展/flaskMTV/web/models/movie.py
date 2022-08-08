#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : movie.py

from datetime import datetime,timedelta
from application import db


class Movie(db.Model):
    """电影表"""
    #id
    id = db.Column(db.Integer,primary_key=True)
    #电影名称
    name = db.Column(db.String(40),unique=True)
    # 演员
    cast = db.Column(db.String(100))
    # 票数
    votes = db.Column(db.Integer, default=0)

class Message(db.Model):
    """评论表"""
    #id
    id = db.Column(db.Integer,primary_key=True)
    #内容
    content = db.Column(db.String(500))
    # 时间
    cast = db.Column(db.DATETIME,default=datetime.now())

