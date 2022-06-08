#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 05-定位元素.py
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    executable_path='./chromedriver.exe'
)

driver.get("https://www.baidu.com/")

#获取输入文本框，id为kw
# driver.find_element_by_id('kw').send_keys("python爬虫")
# driver.find_element_by_css_selector('#kw').send_keys("python爬虫")
driver.find_element_by_xpath('//input[@id="kw"]').send_keys("陈艺文")
time.sleep(2)
#点击百度一下
driver.find_element_by_class_name('s_btn').click()
time.sleep(2)


#查找元素
print(driver.find_elements(By.ID,'kw').text())
# print(driver.find_elements(By.CLASS_NAME,'s_ipt'))
#




