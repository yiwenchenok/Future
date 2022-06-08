#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 07-窗口关闭.py
from selenium import webdriver

driver = webdriver.Chrome(
    executable_path='./chromedriver.exe'
)
driver.get("https://fanyi.baidu.com/")

#关闭当前窗口
# driver.close()

#退出浏览器
driver.quit()