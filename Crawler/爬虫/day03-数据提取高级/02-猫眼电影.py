#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 02-猫眼电影.py
import requests
import re
import json
import os
import time

class MaoyanSpider():
    def __init__(self):
        self.header = {
            'Host': 'maoyan.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
        }
        self.data_lis =[] #存储所有的电影信息
        self.save_path = '猫眼电影.json'


    def get_html(self,url='https://maoyan.com/board/4?offset=0'):

        resp = requests.get(url,headers=self.header)
        html = resp.text
        return html
    def parse(self,html):
        re_lis = re.findall(r'<dd>([\s\S]*?)</dd>', html)  #获取当前页面的所有dd,返回list
        for dd in re_lis:
            dic = {}
            s_name = re.compile('<p class="name"><a href=".*?" title=".*?" data-act="boarditem-click" data-val="{.*?}">(.*?)</a></p>')
            s_star = re.compile('<p class="star">([\s\S]*?)</p>')
            s_releasetime = re.compile('<p class="releasetime">([\s\S]*?)</p>')

            dic['name'] = s_name.findall(dd)[0]
            dic['star'] = s_star.findall(dd)[0].strip()
            dic['releasetime'] = s_releasetime.findall(dd)[0]

            self.data_lis.append(dic)

    def start_spider(self):
        for off in range(0, 100, 10):
            url = f'https://maoyan.com/board/4?offset={off}'
            print("当前爬取页面：",url)
            html = self.get_html(url)
            self.parse(html)
            time.sleep(5)
            print(len(self.data_lis))

        with open(self.save_path, 'w', encoding='utf-8-sig') as f:
            json.dump(self.data_lis, f, ensure_ascii=False)

if __name__ == '__main__':
    ms = MaoyanSpider()
    ms.start_spider()






