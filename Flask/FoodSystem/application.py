# -*- coding: utf-8 -*-
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
import os
import pymysql  # pip install pymysql

pymysql.install_as_MySQLdb()
db = SQLAlchemy()


class MyFlask(Flask):
    def __init__(self, import_name, template_folder=None, root_path=None):
        super(MyFlask, self).__init__(import_name,
                                      template_folder=template_folder,
                                      static_folder=None,  # 让原始的static路径失效，自己在www中注册自定义的static
                                      root_path=root_path,  # app的位置
                                      )
        self.config.from_pyfile('config/base_setting.py')
        if "configName" in os.environ:
            self.config.from_pyfile(f"config/{os.environ['ops_config']}_setting.py")

            """
            ops_config是选择local|production中的一个
            linux系统： export configName=production && python manage.py runserver
            """
        else:  # 默认运行用线下模型
            self.config.from_pyfile('config/local_setting.py')
        db.init_app(self)


db = SQLAlchemy()

import os

template_folder = os.getcwd() + "/web/templates/"  # os.getcwd()返回当前工作目录
app = MyFlask(__name__, template_folder=template_folder, root_path=os.getcwd())  # 重写模板储存目录
manager = Manager(app)

'''
函数模板
'''
from common.libs.UrlManager import UrlManager

app.add_template_global(UrlManager.buildStaticUrl, 'buildStaticUrl')  # 返回静态文件地址
app.add_template_global(UrlManager.buildUrl, 'buildUrl')  # 返回本身
app.add_template_global(UrlManager.buildImageUrl, 'buildImageUrl')  ##图片的地址
