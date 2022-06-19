#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : urls.py
from django.conf.urls import url
from .views import *

urlpatterns = [
    #http://127.0.0.1:8888/person/save_user/jjjjj
    url('save_user/(\w+)',save_user,name='save_user'),
    url('delete_user/(\d+)',delete_user,name='delete_user'),
    url('index/',index),
]
