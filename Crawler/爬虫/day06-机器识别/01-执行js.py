#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 01-执行js.py
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://hao123.com")


#弹窗操作
js = "window.alert('欢迎来到羊驼老师的课堂')"
driver.execute_script(js)


time.sleep(5)

#弹窗的确定取消
a = driver.switch_to.alert
# a.accept()  #点击确定
a.dismiss()  #点击取消


#修改样式
driver.get("http://www.baidu.com") #访问地址
js = 'var kw = document.getElementById("kw");kw.style.border = "10px solid red";'
driver.execute_script(js)




