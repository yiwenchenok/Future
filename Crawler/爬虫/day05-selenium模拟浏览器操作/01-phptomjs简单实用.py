#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 01-phptomjs简单实用.py

#安装selenium
# pip install selenium

from selenium import webdriver

#无界面浏览器
driver = webdriver.PhantomJS(
    executable_path=r'E:\Environment\phantomjs-2.1.1-windows\bin\phantomjs.exe'
)

driver.get("http://www.baidu.com") #访问地址
driver.save_screenshot('baidu.png')  #浏览器截屏
driver.get("http://www.hao123.com") #访问地址
driver.save_screenshot('hao123.png')  #浏览器截屏
print(driver.page_source)  #获取源码




