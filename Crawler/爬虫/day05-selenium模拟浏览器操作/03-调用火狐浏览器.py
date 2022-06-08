#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 02-调用谷歌浏览器.py

#todo:下载对应的谷歌浏览器版本的驱动器

from selenium import webdriver

driver = webdriver.Firefox(
    executable_path='./geckodriver.exe'
)

driver.get("http://www.baidu.com") #访问地址
driver.save_screenshot('baidu3.png')  #浏览器截屏
