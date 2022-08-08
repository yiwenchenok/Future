#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 20:50
# @Author  : 羊驼
# @File    : manage.py
# @Software: PyCharm
from flask_migrate import Migrate, MigrateCommand #pip install flask-migrate==2.7.0
from flask_script import Manager
from movie import app,db



manager = Manager(app) #命令行管理工具
Migrate(app,db)  #关联app,db
manager.add_command("db",MigrateCommand) #将迁移命令添加到命令行管理工具

if __name__ == '__main__':
    print(app.url_map)
    manager.run()
