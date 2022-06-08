#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 11-利用保存的cookie来登录.py
import time

from selenium import webdriver
import json

driver = webdriver.Chrome(executable_path="./chromedriver.exe")
url = 'https://www.cnki.net/?PlatForm=kns'
driver.get(url)
driver.maximize_window()
#写入cookie
with open("zhiwang.json",'r') as f:
    for i in f:
        cookie = json.loads(i)
        driver.add_cookie(cookie)
# print(driver.get_cookies())

index_url = "https://www.cnki.net/?PlatForm=kns"
driver.get(index_url)
print('写入cookie成功')
time.sleep(3)
driver.quit()






