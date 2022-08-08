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



class Movie(db.Model):
    """
    电影
    """

    #id主键
    id = db.Column(db.Integer,primary_key=True)
    #名称
    name = db.Column(db.String(20))


    #不是真实存在的字段，为了方便查询创建
    cast = db.relationship("Cast",backref='Movie')

    def __repr__(self):
        return f"Movie:<{self.name}>"




class Cast(db.Model):
    """
    演员
    """

    #id主键
    id = db.Column(db.Integer,primary_key=True)
    #名称
    name = db.Column(db.String(20))
    #外键关联
    movie_id = db.Column(db.Integer,db.ForeignKey("movie.id"))

    def __repr__(self):
        return f"Cast:<{self.name}>"



if __name__ == '__main__':

    db.drop_all()  # 删除所有表，物理删除，生产环境下勿用
    db.create_all()  #创建所有表


    m1 = Movie()
    m1.name = "大话西游"
    m2 = Movie(name = "功夫")
    db.session.add_all([m1,m2])
    db.session.commit()

    cast_list = []
    for i in ['周星驰', '朱茵', '吴孟达', '莫文蔚',"牛夫人"]:
        c = Cast(name=i, movie_id=m1.id)
        cast_list.append(c)

    for i in ['周星驰', '梁小龙', '元华']:
        c = Cast(name=i, movie_id=m2.id)
        cast_list.append(c)

    db.session.add_all(cast_list)
    db.session.commit()

















