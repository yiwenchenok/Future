#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 02-调用谷歌浏览器.py

#todo:下载对应的谷歌浏览器版本的驱动器
import time
from selenium import webdriver

driver = webdriver.Chrome(
    executable_path='./chromedriver.exe'
)
driver.maximize_window()#全屏打开
driver.get("http://www.baidu.com") #访问地址
driver.save_screenshot('baidu2.png')  #浏览器截屏
driver.get("http://www.hao123.com") #访问地址
driver.save_screenshot('hao1232.png')  #浏览器截屏
time.sleep(5)
driver.close()
# print(driver.page_source)  #获取源码
