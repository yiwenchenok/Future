#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : main.py
from scrapy.cmdline import execute

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute('scrapy crawl quotes_c -o quotes_c.csv'.split(" "))
