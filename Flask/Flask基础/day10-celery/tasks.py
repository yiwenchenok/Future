#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : tasks.py
from celery import Celery
import time

# 创建celery实例，配置celery中间人，我们使用redis. # backend 指定保存结果,指定保存在redis中。
app = Celery('c_test',broker='redis://127.0.0.1:6379/4',backend='redis://127.0.0.1:6379/5')
# app = Celery('c_test')

#配置方式1：update
# app.conf.update(
#     broker_url='redis://127.0.0.1:6379/4',
#     result_backend='redis://127.0.0.1:6379/5'
# )

#配置方式2： 类
class Config:
    broker_url='redis://127.0.0.1:6379/4'
    result_backend='redis://127.0.0.1:6379/5'
#加载配置类
app.config_from_object(Config)

#配置方式3：py文件，见示例celery_test

# 通过celery实例装饰任务函数
@app.task
def task():
    time.sleep(10)
    print("celery异步任务1")
    return 1

# 通过celery实例装饰任务函数
@app.task
def task2():
    time.sleep(10)
    print("celery异步任务2")
    return 2


#进入命令行
#celery -A tasks worker -l info --pool=solo 进入工作者模式
#另起命令行
#from tasks import task,task2
#task.delay() #包工头
