# -*- coding: utf-8 -*-
DEBUG = True
SQLALCHEMY_ECHO = False #是记录打印SQL语句用于调试的, 一般设置为False, 不然会在控制台输出一大堆的东西
SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1/food_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENCODING = "utf8"
