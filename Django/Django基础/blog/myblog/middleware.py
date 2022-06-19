#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : middleware.py
from django.http import HttpResponse,HttpResponseForbidden

class YTMiddleware:
    def __init__(self):
        """
        只会执行一次，第一次请求的时候，后面就不再执行
        """
        print("__init__执行")

    def process_request(self, request):
        """
        构造好请求之后，在匹配视图之前执行，返回None（默认）将继续执行，如果返回HttpResponse对象将直接返回给浏览器
        经常用作拦截器
        :param request:
        :return:
        """
        # black_list = ['127.0.0.1','192.168.0.100']
        black_list = []

        client_ip = request.META.get("REMOTE_ADDR")  #获取用户的ip
        if client_ip in black_list:
            # return HttpResponse("fuck spider")
            return HttpResponseForbidden("403")

        print('process_request执行')

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        匹配视图之后，但是在执行视图之前执行
        :param request: 请求对象
        :param view_func: 视图函数
        :param view_args: 视图函数的位置参数
        :param view_kwargs: 视图函数中的关键字参数
        :return: 返回None，将继续执行视图函数，如果返回HttpResponse则直接返回给浏览器
        """
        print('process_view执行')

    def process_template_response(self, request, response):  #bug，windows下不会打印
        """
        执行完视图之后，在处理模板响应之前执行
        :param request: 请求对象
        :param response: 响应对象
        :return: 必须返回一个httpresponse
        """
        print('process_template_response执行')

        return response

    def process_response(self, request, response):
        """
        返回数据给浏览器之前执行
        :param request:
        :param response:
        :return:  返回response
        """
        print('process_response执行')

        return response

    def process_exception(self,request,exception):
        """
        当视图函数抛出异常时执行，需要返回httpresponse对象
        :param request:
        :param exception:
        :return:
        """
        return HttpResponse("视图函数抛出异常")
