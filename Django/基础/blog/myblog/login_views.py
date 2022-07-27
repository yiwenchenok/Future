#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : login_views.py
from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import View


def check_login(request):
    user = "admin"
    pwd_ = '1'

    username = request.POST.get("username")
    pwd = request.POST.get("pwd")

    if user == username and pwd_ == pwd:
        #登录成功
        # return HttpResponse("succsess")
        #重定向到主页
        # return redirect('/index')
        # return redirect(reverse('index')) #根据name反射路由
        # return redirect('/index/get_cookie/')
        return redirect(reverse('get_cookie')) #根据name反射路由
    else:
        return render(request, 'myblog/login.html', context={"is_login":0, 'username':username, 'pwd':pwd})


def login(request):
    """
    登录验证
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, 'myblog/login.html', context={"is_login":1})  #如果是login页面就不显示提示
    elif request.method == "POST":
        user = "admin"
        pwd_ = '1'
        username = request.POST.get("username")
        pwd = request.POST.get("pwd")

        if user == username and pwd_ == pwd:
            return redirect(reverse('get_cookie'))  # 根据name反射路由
        else:
            return render(request, 'myblog/login.html', context={"is_login": 0, 'username': username, 'pwd': pwd})


class Login(View):
    """
    登录验证
    :param request:
    :return:
    """
    def get(self,request):
        return render(request, 'myblog/login.html', context={"is_login": 1})  # 如果是login页面就不显示提示
    def post(self, request):
        user = "admin"
        pwd_ = '1'
        username = request.POST.get("username")
        pwd = request.POST.get("pwd")
        if user == username and pwd_ == pwd:
            return redirect(reverse('get_cookie'))  # 根据name反射路由
        else:
            return render(request, 'myblog/login.html', context={"is_login": 0, 'username': username, 'pwd': pwd})








