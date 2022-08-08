# -*-coding:utf-8-*-
# Autor:编程的小姐姐
# DateTime:2022/4/26 20:12
# File:01-数据库连接
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

class MyConfig:
    SECRET_KEY = "dalkgjklajglkajg"
    PROJECT_PATH  = os.path.dirname(__file__)
    print("PROJECT_PATH:",PROJECT_PATH) #C:/Users/Administrator/Desktop/py418Dj/day06-flask模型
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{PROJECT_PATH}/learn'  #数据库连接
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:密码@127.0.0.1:3306/py418'  #mysql数据库连接
    SQLALCHEMY_TRACK_MODIFICATIONS = True #跟踪数据库修改


app.config.from_object(MyConfig)


#创建数据库连接，并且管理项目
db = SQLAlchemy(app)

class User(db.Model):
    """
    创建模型类
    """
    id = db.Column(db.INTEGER,primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(40))



if __name__ == '__main__':
    # app.run(debug=True)


    db.drop_all()  #删除所有表，物理删除，生产环境下勿用

    db.create_all()#创建表