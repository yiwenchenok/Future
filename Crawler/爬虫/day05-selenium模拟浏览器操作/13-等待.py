#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 13-等待.py

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



driver = webdriver.Chrome(executable_path="./chromedriver.exe")
index_url = "https://www.cnki.net/?UID=WEEvREcwSlJHSldTTEYzWEpEYnphMFR4MThweldhSlI3VnBRZG1PbWE3TT0%3d%249A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&PlatForm=kns"
driver.get(index_url)

#隐式等待 相当于time.sleep(10)
driver.implicitly_wait(3)
driver.get("http://wwww.baidu.com")

#显示等待，等到某一个元素出现之后,如果3秒没出现，则会报错
WebDriverWait(driver,3).until(EC.presence_of_element_located((By.ID,"kw")))
driver.find_element_by_id('kw').send_keys("不掉发的羊驼")


time.sleep(3)
driver.refresh() #刷新




