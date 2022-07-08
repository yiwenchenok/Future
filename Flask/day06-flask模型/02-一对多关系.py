# -*-coding:utf-8-*-
# Autor:编程的小姐姐
# DateTime:2022/4/26 21:06
# File:02-一对多关系
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
class MyConfig:
    PROJECT_PATH  = os.path.dirname(__file__)
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{PROJECT_PATH}/learn'  #数据库连接
    SQLALCHEMY_TRACK_MODIFICATIONS = True #跟踪数据库修改
app.config.from_object(MyConfig)




db = SQLAlchemy(app)



class Father(db.Model):
    __tablename__ = "father"
    #id主键
    id = db.Column(db.Integer,primary_key=True)
    #名称
    name = db.Column(db.String(20),unique=True)
    #不是真实存在的字段，为了方便查询创建
    s = db.relationship("Son",backref='father')



class Son(db.Model):
    __tablename__ = "son"
    #id主键
    id = db.Column(db.Integer,primary_key=True)
    #名称
    name = db.Column(db.String(20),unique=True)
    #外键关联
    father_id = db.Column(db.Integer,db.ForeignKey("father.id"))


if __name__ == '__main__':
    db.drop_all()  # 删除所有表，物理删除，生产环境下勿用


    db.create_all()  #创建所有表

    f = Father()
    f.name = "盖伦3333"
    db.session.add(f) #将数据对象提交到会话
    db.session.commit() #写入数据库


    s = Son()
    s.name = "大头儿子3333"
    s.father_id = f.id


    db.session.add(s) #将数据对象提交到会话
    db.session.commit() #写入数据库














