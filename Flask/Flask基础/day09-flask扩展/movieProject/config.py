#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 20:52
# @Author  : 羊驼
# @File    : config.py
# @Software: PyCharm


#配置基础类
class BaseConfig:
    GUOQISHIJIAN = 10  #session过期时间
    SECRET_KEY = "fljlkjsklh"

class LocalConfig(BaseConfig):
    """本地配置"""
    DEBUG =True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/py418'

class ProductConfig(BaseConfig):
    """线上配置"""
    DEBUG =False
    SQLALCHEMY_DATABASE_URI = 'mysql://root:xxxxx@xxxxxx:3306/py418'



CONFIG = {
    "local":LocalConfig,
    "product":ProductConfig,
}
