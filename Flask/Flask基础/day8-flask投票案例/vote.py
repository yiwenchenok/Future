#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/30 20:22
# @Author  : 羊驼
# @File    : vote.py
# @Software: PyCharm
from datetime import datetime,timedelta
from flask import Flask,render_template,request,session,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand #pip install flask-migrate==2.7.0
from flask_script import Shell,Manager
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
import time

import pymysql  #pip install pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)

#配置类
class Config:
    GUOQISHIJIAN = 10  #session过期时间
    DEBUG =True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/py418'
    SECRET_KEY = "fljlkjsklh"

#加载配置信息
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config.from_object(Config)

#命令行管理工具
manager = Manager(app)
#创建数据库连接
db = SQLAlchemy(app)
#迁移关联
Migrate(app,db)
manager.add_command('db',MigrateCommand) #将迁移命令添加到命令工具


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
    time = db.Column(db.DATETIME,default=datetime.now())


class MsgForm(FlaskForm):
    """form表单"""
    content = StringField(label="留言",validators=[DataRequired()])
    submit = SubmitField(label="提交")


@app.route('/',methods=["get","post"])
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

            return render_template("vote.html", **context)



# @app.route("/voted")
# def voted():
#     """get请求传参"""
#     #获取电影id
#     mid = request.args.get('m_id')
#     #查询对应电影
#     m = Movie.query.get(mid)
#     #票数+1
#     m.votes +=1
#     #提交数据保存到数据库
#     db.session.add(m)
#     db.session.commit()
#
#     return redirect("/")


@app.route("/vote/<int:id>")
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
        app.permanent_session_lifetime = timedelta(seconds=app.config["GUOQISHIJIAN"])

        #保存session为1天之后的时间撮
        # session["is_vote"] = time.time() + 24*60*60
        session["is_vote"] = time.time() + app.config["GUOQISHIJIAN"]

    return redirect("/")  #重定向到index

if __name__ == '__main__':
    ''' 1.创建迁移仓库
        python 项目名.py db init
        2.生成迁移文件
        python 项目名.py db migrate
        3.执行迁移文件生成数据表
        python 项目名.py db upgrade 
    '''
    manager.run()
