#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : start.py
from scrapy import cmdline

cmdline.execute('scrapy crawl gz -o 58.csv'.split(' '))
