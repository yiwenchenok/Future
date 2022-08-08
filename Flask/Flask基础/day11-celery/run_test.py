#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/9 20:26
# @Author  : 羊驼
# @File    : run_test.py
# @Software: PyCharm
from celery_test.tasks import *
from celery import group,chain

# s = task1.signature((1,12),queue="myqueque")
# s.delay()


#任务组
# g = group(
#     task1.signature((1, 12), queue="myqueque"),
#     task2.signature((1, 12), queue="myqueque"),
#     task3.signature((1, 12), queue="myqueque"),
#     task4.signature((1, 12), queue="myqueque"),
# )
#
# result = g.delay()
# print(result.get())

#任务链
# ch = chain(
#     task1.signature((1, 12), queue="myqueque")| task2.signature((12,), queue="myqueque"))
#
#
# result = ch.delay()
# print(result.get())




#任务路由的展示
res = upload_img.delay()
print(res.get())

res = handle_img.delay()
print(res.get())

res = send_message.delay()
print(res.get())