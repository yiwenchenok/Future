#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 04-爬虫小案例-糗事百科段子.py
import requests
from bs4 import BeautifulSoup
import chardet   #pip install chardet
import random
class Qiushi():
    def __init__(self):
        self.url = "https://www.qiushibaike.com/text/page/3/"

        #构造请求头
        self.header = {
            "Host": "www.qiushibaike.com",
            "Referer": "https://www.qiushibaike.com/text/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        }
        #构造代理
        """
        222.212.175.64	7890	高匿名	HTTP	中国 四川 成都 电信	秒	2021-11-05 20:31:01
        43.228.180.60	80	高匿名	HTTP	中国 香港 bih.cn	秒	2021-11-05 19:31:01
        180.122.147.14	3000	高匿名	HTTP	中国 江苏 泰州 电信	0.4秒	2021-11-05 18:31:01
        119.28.51.186	59394	高匿名	HTTP	中国 香港 tencent.com	2秒	2021-11-05 17:31:01
        """
        self.proxies = [
            {'http':"http://222.212.175.64:7890",},
            {'http':"http://43.228.180.60:80",},
            {'http':"http://180.122.147.14:3000",},
            {'http':"http://119.28.51.186:59394",}
        ]

    def get_html(self):
        """
        发送请求
        :return: response.text
        """
        response = requests.get(self.url,headers=self.header,
                                proxies=random.choice(self.proxies))

        if response.status_code == 200:
            #两种方式获取源码的编码格式
            #方法1requests.utils.get_encodings_from_content:
            print(requests.utils.get_encodings_from_content(response.text)) #获取网站编码 ['utf-8']
            #方法2
            print(response.apparent_encoding) #成功率98%
            #方法3
            print(chardet.detect(response.content))
            # response.encoding = response.apparent_encoding
            return response.text

    def parse_html(self,html):
        soup = BeautifulSoup(html, "lxml")
        dz_list = soup.select(".old-style-col1 > .article")
        for item in dz_list:
            author = item.select("h2")[0].get_text().strip()
            content = item.select(".content > span")[0].get_text().strip()
            smile = item.select(".stats > .stats-vote > i")[0].get_text().strip()
            comments = item.select(".stats > .stats-comments i")[0].get_text().strip()

            data = {
                "author":author,
                "content":content,
                "smile":smile,
                "comments":comments,
            }
            yield data  #生成器

    def save(self,data):
        with open("糗事百科段子.txt","a",encoding='utf-8') as f:
            f.write(" ".join(data.values())+'\n')
            f.write("我是换行符".center(100,"*")+'\n')

if __name__ == '__main__':
    q = Qiushi()
    html = q.get_html()
    data_yield = q.parse_html(html)
    for data in data_yield:
        q.save(data)




