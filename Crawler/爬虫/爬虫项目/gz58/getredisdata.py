#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : getredisdata.py
import pandas as pd
from redis import *
# host = Redis服务器地址
# port = 6379 redis服务端口号，默认6379
# db = 0 连接那个数据库（0-15）
st = StrictRedis(host='127.0.0.1', port=6379, db=0)
res = st.keys() # 查看所有key
print(res)
len_data = st.llen("gz:items") #获取数据的长度
print(len_data)  #获取数据长度
data_lis = []
for i in range(len_data):
    data = eval(st.lpop("gz:items").decode()) ## 移除列表第一个元素并返回
    data_lis.append(data)

df = pd.DataFrame(data_lis)
df.to_csv('save.csv',index=False)
