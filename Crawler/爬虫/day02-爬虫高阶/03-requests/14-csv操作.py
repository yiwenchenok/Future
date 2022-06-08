#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 14-csv操作.py

import csv

data = [
    {'id':1,'语文':80,'数学':90},
    {'id':2,'语文':83,'数学':95},
    {'id':3,'语文':82,'数学':97},
    {'id':4,'语文':81,'数学':60},
    {'id':5,'语文':88,'数学':80},
]

f = open('socre.csv','w',encoding='gbk',newline='')

write = csv.writer(f,delimiter=',') #默认逗号分隔

for i,dic in enumerate(data,start=1):
    if i == 1: #第一行写表头
        write.writerow(dic.keys())
        # write.writerow(['id','语言','数学'])
    #写入数据
    write.writerow(dic.values())

f.close()

