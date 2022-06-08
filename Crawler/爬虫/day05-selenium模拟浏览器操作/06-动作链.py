#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 06-动作链.py
from selenium import webdriver
import time
from selenium.webdriver import ActionChains #动作链
driver = webdriver.Chrome(
    executable_path='./chromedriver.exe'
)
driver.get("https://fanyi.baidu.com/")
driver.find_element_by_class_name('desktop-guide-close').click() #去广告
#定位到 select-inner
select_inner = driver.find_element_by_class_name('select-inner')
#点击
ActionChains(driver).move_to_element(select_inner).click().perform()

#从一个元素移动到另外一个元素
trans_btn = driver.find_element_by_class_name('trans-btn')
ActionChains(driver).drag_and_drop(select_inner,trans_btn).context_click().perform() #context_click鼠标右击

driver.get("http://www.baidu.com")
in_id = driver.find_element_by_id('kw')
# 鼠标hold住
ActionChains(driver).move_to_element(in_id).click_and_hold().perform()


ActionChains(driver).release()  #释放鼠标