#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 15-追加csv.py

import csv

f = open('socre.csv','a',encoding='gbk',newline='')
write = csv.writer(f)

write.writerow([100,85,67])

f.close()
