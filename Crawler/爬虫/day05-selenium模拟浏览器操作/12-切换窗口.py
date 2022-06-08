#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 12-切换窗口.py
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="./chromedriver.exe")
index_url = "https://www.cnki.net/?UID=WEEvREcwSlJHSldTTEYzWEpEYnphMFR4MThweldhSlI3VnBRZG1PbWE3TT0%3d%249A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&PlatForm=kns"
driver.get(index_url)


driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/ul/li[2]/a').click()

#获取所有窗口
all_windows = driver.window_handles


#切换到某一个窗口进行关闭
driver.switch_to_window(all_windows[1])  #0表示第一个窗口
time.sleep(5)
driver.close()



