# -*-coding:utf-8-*-
# Autor:编程的小姐姐
# DateTime:2022/4/26 21:31
# File:04-多对多关系
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)


class MyConfig:
    PROJECT_PATH = os.path.dirname(__file__)
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{PROJECT_PATH}/learn'  # 数据库连接
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # 跟踪数据库修改


app.config.from_object(MyConfig)

db = SQLAlchemy(app)

# 多对多关系的中间表
secondary_table = db.Table('secondary_table',
                           db.Column("author_id",db.Integer, db.ForeignKey('author.id')),
                           db.Column("book_id",db.Integer, db.ForeignKey('book.id')),
                           )


class Author(db.Model):
    __tablename = "author"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    #relationship字段需要跟数据库名称同名,back_populates指定关联表，secondary指定中间表
    book = db.relationship("Book",back_populates='author', secondary=secondary_table)



class Book(db.Model):
    __tablename = "book"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    #relationship字段需要跟数据库名称同名,back_populates指定关联表，secondary指定中间表
    author = db.relationship("Author",back_populates='book', secondary=secondary_table)


if __name__ == '__main__':
    db.create_all() #创建所有表



    a = Author()
    a.name = "羊驼"
    a2 = Author()
    a2.name = "小白"
    a3 = Author()
    a3.name = "小黑"

    #同时添加多个数据对象到会话
    db.session.add_all([a,a2,a3])
    db.session.commit()  # 写入数据库


    b = Book()
    b.name = "西游记"

    #多对多关系添加数据
    b.author.append(a2)
    b.author.append(a3)
    db.session.add(b) #将数据对象提交到会话
    db.session.commit() #写入数据库


