#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 08-模拟登录知网.py
from selenium import webdriver
import time

url = 'https://login.cnki.net/login/?platform=kns&ForceReLogin=1&ReturnURL=https://www.cnki.net/'

driver = webdriver.Chrome(executable_path="./chromedriver.exe")
driver.get(url)

driver.maximize_window()#全屏打开
#写入登录用户名
driver.find_element_by_id('TextBoxUserName').send_keys('13318011750')
#写入登录密码
driver.find_element_by_id('TextBoxPwd').send_keys('5560318abcd')
time.sleep(1)
#点击登录
driver.find_element_by_id('Button1').click()
time.sleep(3)
html = driver.page_source
print(html.find("13318011750"))  #返回位置
driver.back()  #后退
time.sleep(3)
driver.forward()  #前进
time.sleep(3)



