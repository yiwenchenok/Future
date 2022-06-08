#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : main.py
from scrapy.cmdline import execute

import sys
import os

execute('scrapy crawl sina'.split(" "))
