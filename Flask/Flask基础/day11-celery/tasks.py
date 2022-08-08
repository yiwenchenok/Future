#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/9 20:20
# @Author  : 羊驼
# @File    : tasks.py
# @Software: PyCharm
import time
from celery import Celery

app = Celery("c_test")

#update方式配置
# app.conf.update(
#     broker_url='redis://127.0.0.1:6379/8',
#     result_backend='redis://127.0.0.1:6379/9'
# )

#创建类的方式配置
class Myconfig:
    broker_url='redis://127.0.0.1:6379/8',
    result_backend='redis://127.0.0.1:6379/9'
app.config_from_object(Myconfig)




#通过celery实例装饰任务函数
@app.task
def task(a,b):
    time.sleep(3)
    print("celery,异步任务")
    return a + b
