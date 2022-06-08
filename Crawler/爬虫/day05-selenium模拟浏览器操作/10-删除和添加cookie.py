#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 10-删除和添加cookie.py
from selenium import webdriver
import time
import json
url = 'https://login.cnki.net/login/?platform=kns&ForceReLogin=1&ReturnURL=https://www.cnki.net/'
driver = webdriver.Chrome(executable_path="./chromedriver.exe")
driver.get(url)
# 写入登录用户名
driver.find_element_by_id('TextBoxUserName').send_keys('13318011750')
# 写入登录密码
driver.find_element_by_id('TextBoxPwd').send_keys('5560318abcd')
# 点击登录
driver.find_element_by_id('Button1').click()
time.sleep(3)
html = driver.page_source
print(html.find("13318011750"))  # 返回位置
print(driver.get_cookies())  # 获取所有的cookie
#todo；登录成功后，保存cookie 一般网站登录持久化，借助cookie来实现
with open("zhiwang.json",'w') as f:
    for cookie in driver.get_cookies():
        cookie_json = json.dumps(cookie)
        f.write(cookie_json+"\n")
# 删除cookie
driver.delete_cookie('Ecp_notFirstLogin')
print(driver.get_cookies())  # 获取所有的cookie
# 删除所有cookie
driver.delete_all_cookies()
print(driver.get_cookies())  # 获取所有的cookie
# 设置cookie  必须有value
driver.add_cookie({
    'name': 'Ecp_notFirstLogin',
    'value': 'yangtuo',
})
# print(driver.get_cookies())  # 获取所有的cookie

