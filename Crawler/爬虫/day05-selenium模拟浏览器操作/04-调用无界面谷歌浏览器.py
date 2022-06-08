#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 02-调用谷歌浏览器.py

#todo:下载对应的谷歌浏览器版本的驱动器

from selenium import webdriver
#实现无可视化界面的操作
from selenium.webdriver.chrome.options import Options

chrom_options = Options()
chrom_options.add_argument("--headless") #创建无界面chrome
chrom_options.add_argument("--disable-gpu")


driver = webdriver.Chrome(
    executable_path='./chromedriver.exe',
    chrome_options=chrom_options,
)

driver.get("http://www.baidu.com") #访问地址
driver.save_screenshot('baidu3.png')  #浏览器截屏
driver.get("http://www.hao123.com") #访问地址
driver.save_screenshot('hao1233.png')  #浏览器截屏
