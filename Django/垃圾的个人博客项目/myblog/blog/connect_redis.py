#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : connect_redis.py

from redis import StrictRedis
from django.conf import settings

class MyRedis():
    #创建连接
    conn = StrictRedis(host=settings.REDIS_HOST,port=settings.REDIS_PORT,db=0)
    def set(self,key,value):
        """插入数据"""
        self.conn.set(key,value,ex=60*60)
    def get(self,key):
        """获取数据"""
        return self.conn.get(key)

