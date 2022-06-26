#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : middleware.py
from django.http import HttpResponse
from .connect_redis import MyRedis
import time
from myblog.settings import IP_NUMS


class YTMiddleware:
    def process_request(self, request):
        """
        构造好请求之后，在匹配视图之前执行，返回None（默认）将继续执行，如果返回HttpResponse对象将直接返回给浏览器
        经常用作拦截器
        :param request:
        :return:
        """
        #获取用户的ip
        cliend_ip = request.META.get("REMOTE_ADDR")
        #连接redis
        redis = MyRedis()
        #尝试从redis中获取key cliend_ip的值
        value = redis.get(cliend_ip)
        if not value:
            #第一次访问,可以将其访问存储到redis,字符串拼接时间撮和访问次数
            redis.set(cliend_ip,str(time.time())+"|1")
        else:
            r_time,num = value.decode("utf-8").split("|")

            #如果1秒之内访问记录超过10次就认为是访问过量
            if time.time() -float(r_time) <= 1:  #小于1秒
                if int(num) > IP_NUMS:  #todo:重要的一个参数，限制一秒点击多少次
                    return HttpResponse("访问太过频繁，请稍后访问")
                else:
                    redis.set(cliend_ip, str(time.time()) + f"|{int(num) + 1}")
            else: #大于1秒
                if int(num) >IP_NUMS: #如果已经进入黑名单，让其20秒之后才访问
                    if abs(time.time()-float(r_time)) >= 20:
                        redis.set(cliend_ip, str(time.time()) + "|1")
                    else:
                        return HttpResponse("访问太过频繁，请稍后访问")
                else:
                    redis.set(cliend_ip, str(time.time()) + "|1") #重新统计



