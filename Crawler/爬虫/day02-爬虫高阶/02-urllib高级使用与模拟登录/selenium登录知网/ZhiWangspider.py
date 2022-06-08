#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : Googlespider.py

import os
import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import pandas as pd

USERNAME = os.environ['USERNAME']  #当前使用用户


class ZhiWangSelenuim:
    def __init__(self, username="249084156@qq.com", pwd='admin123456'):
        super().__init__()
        self.username = username
        self.pwd = pwd
        self.option = webdriver.ChromeOptions() #需要下载跟自己浏览器版本对应的谷歌插件 http://chromedriver.storage.googleapis.com/index.html
        self.option.add_argument("disable-gpu")
        self.option.add_experimental_option("detach", True) #运行完不关闭浏览器，不报错的情况下
        self.driver = webdriver.Chrome(options=self.option)  # 以上为浏览器对象创建
        self.url = 'https://login.cnki.net/login/?platform=kns&ForceReLogin=1&ReturnURL=https://www.cnki.net/'

    def start_project_keywords_get_html(self):
        self.driver.get(self.url)
        search_input1 = self.driver.find_element_by_name('TextBoxUserName')
        search_input1.send_keys(self.username)  #获取搜索框并写入内容
        search_input2 = self.driver.find_element_by_name('TextBoxPwd')
        search_input2.send_keys(self.pwd)  #获取搜索框并写入内容
        condition_1 = EC.visibility_of_element_located((By.ID, "Button1"))# 等待按钮出现,name为btnK
        WebDriverWait(self.driver, timeout=20,poll_frequency=0.5).until(condition_1)# 按钮出现后点击
        google_button = self.driver.find_element_by_id("Button1")
        google_button.send_keys(Keys.ENTER)

        #页面自动跳转向另一页，确保一下看是否有这个导航栏 top_nav,谷歌搜索的每一个页面都会有这个
        condition_4 = EC.visibility_of_element_located( (By.ID, 'Ecp_loginShowName'))
        WebDriverWait(self.driver, timeout=20, poll_frequency=0.5).until(condition_4)
        return self.driver.page_source #可以不返回，用self.driver.find_element(By.XPATH，xpath)不需要返回这个



    def wait_and_click(self, xpath): #todo:等待和点击
        # 等待元素出现并点击，异常的捕获，处理点击时没响应的情况
        try:
            w = WebDriverWait(self.driver, 15)
            elem = w.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            elem.click()
            # self.highlight(elem)
        except Exception as e:
            print("异常信息：",e)
            print('点击响应超时 - {}'.format(xpath))
            print('刷新浏览器...')
            self.driver.refresh()
            time.sleep(2)
            return self.wait_and_click(xpath)
        return elem



zs = ZhiWangSelenuim()
print(zs.start_project_keywords_get_html())



























