#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 21:06
# @Author  : 羊驼
# @File    : vote.py
# @Software: PyCharm
from datetime import timedelta
from flask import render_template,request,session,redirect,Blueprint,current_app
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
import time
from movie.models import *
vote_app = Blueprint("vote_app",__name__)


class MsgForm(FlaskForm):
    """form表单"""
    content = StringField(label="留言",validators=[DataRequired()])
    submit = SubmitField(label="提交")


@vote_app.route('/',methods=["get","post"])
def index():
    #创建一个表单对象
    form = MsgForm()
    #把所有电影查询出来
    m_all = Movie.query.all()
    msg = Message.query.all()
    context = {
        "m_all":m_all,
        "form":form,
        "msg":msg
    }

    if request.method == "GET":
        return render_template("vote.html",**context)
    else:
        #处理留言
        if form.validate_on_submit(): #校验通过
            data = form.content.data
            ms = Message()
            ms.content = data
            # 提交数据保存到数据库
            db.session.add(ms)
            db.session.commit()
            return redirect("/")
        else: #不通过
            print(form.errors)
            return render_template("vote.html", **context)




@vote_app.route("/vote/<int:id>")
def vote(id):
    """get请求传参"""

    #判断是否能从session获取到is_vote
    is_vote = session.get("is_vote")
    if not(is_vote and float(is_vote) > time.time()): #获取不到就表示第一次请求，或者获取到，但是过了一天时间则可以投票
        #获取电影id
        mid = id
        #查询对应电影
        m = Movie.query.get(mid)
        #票数+1
        m.votes +=1
        #提交数据保存到数据库
        db.session.add(m)
        db.session.commit()

        #用session来保存用户投票时间的时间撮
        session.permanent = True  #session超时时间
        # app.permanent_session_lifetime = timedelta(seconds=24*60*60) #一天过期
        current_app.permanent_session_lifetime = timedelta(seconds=current_app.config["GUOQISHIJIAN"])

        #保存session为1天之后的时间撮
        # session["is_vote"] = time.time() + 24*60*60
        session["is_vote"] = time.time() + current_app.config["GUOQISHIJIAN"]

    return redirect("/")  #重定向到index