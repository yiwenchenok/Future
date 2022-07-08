# -*-coding:utf-8-*-
# Autor:编程的小姐姐
# DateTime:2022/4/26 21:06
# File:02-一对多关系
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
import os
from flask_migrate import Migrate,MigrateCommand


app = Flask(__name__)


class MyConfig:
    PROJECT_PATH  = os.path.dirname(__file__)
    SQLALCHEMY_DATABASE_URI = 'mysql://root:manager@127.0.0.1:3306/py418'  #mysql数据库连接
    SQLALCHEMY_TRACK_MODIFICATIONS = True #跟踪数据库修改
app.config.from_object(MyConfig)
# 自动提交数据库中的改动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# 追踪对象
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


#创建数据库对象
db = SQLAlchemy(app)




#命令行管理器
manager = Manager(app)

#将数据库连接于flask、关联
Migrate(app,db)


#给命令行管理器添加db命令，绑定migrate
manager.add_command('db',MigrateCommand)



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
    """
    需要使用mysql
    第一步：初始化 创建migrations目录
    python 数据库迁移.py db init
    #第二步：生成迁移文件
    python 数据库迁移.py db migrate -m '第一次迁移'
    #第三步：迁移到数据库
    python 数据库迁移.py db upgrade
    """

    # db.create_all()  # 创建所有表



    manager.run()

# if __name__ == '__main__':
#
#     db.drop_all()  # 删除所有表，物理删除，生产环境下勿用
#     db.create_all()  #创建所有表
#
#
#     m1 = Movie()
#     m1.name = "大话西游"
#     m2 = Movie(name = "功夫")
#     db.session.add_all([m1,m2])
#     db.session.commit()
#
#     cast_list = []
#     for i in ['周星驰', '朱茵', '吴孟达', '莫文蔚',"牛夫人"]:
#         c = Cast(name=i, movie_id=m1.id)
#         cast_list.append(c)
#
#     for i in ['周星驰', '梁小龙', '元华']:
#         c = Cast(name=i, movie_id=m2.id)
#         cast_list.append(c)
#
#     db.session.add_all(cast_list)
#     db.session.commit()

















