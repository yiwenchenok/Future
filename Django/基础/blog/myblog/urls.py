#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : urls.py
from django.conf.urls import url
from .views import *
from .login_views import *
urlpatterns = [
    # 子路由：/index/detail
    url('^$', index, name='index'),  # \d+代表一个或者多个数字，（）表示提取
    # url('^$',Index.as_view(),name='index'),  #类视图的写法,效果同上
    # url('^detail/(\d+)',detail,name='detail'),  #\d+代表一个或者多个数字，（）表示提取
    url('^detail/(\d+)', Detail.as_view(), name='detail'),  # 类视图的写法
    # url('^login/',login,name='login'),
    url('^login/', Login.as_view(), name='login'),  # 类视图解析成视图函数
    # url('^check_login/',check_login,name='check_login'),
    url('^req_info/', req_info, name='req_info'),#请求-HttpRequest
    url('^get_info/', get_info, name='get_info'),#get请求
    url('^post_index/', post_index, name='post_index'),#post请求主页
    url('^post_do/', post_do, name='post_do'),#执行post请求
    url('^resp/', resp, name='resp'),#HttpResponse响应
    url('^set_cookie/', set_cookie, name='set_cookie'),
    url('^get_cookie/', get_cookie, name='get_cookie'),
    url('^del_cookie/', del_cookie, name='del_cookie'),
    url('^val/', val, name='val'),#上下文传参

    url('^set_session/', set_session, name='set_session'),
    url('^get_session/', get_session, name='get_session'),
    url('^del_session/', del_session, name='del_session'),
    url('^send_m/$', send_m),#发送少量邮件
    url('^send_m_2/$', send_m_2),#发送大量邮件
    url('^pic_load/$',pic_load),#上传图片
    url('^zy/$',zy),#转义
]
