import os.path
import pprint

from lxml import etree
import requests

if __name__ == "__main__":\
    #1、爬取页面源码数据
    url='https://www.aqistudy.cn/historydata/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
    }
    page_text=requests.get(url=url,headers=headers).text
    tree=etree.HTML(page_text)
    #2.解析数据
    # //div[@class="bottom"]/ul/li/a   热门城市a标签的层级关系
    # //div[@class="bottom"]/ul/div[2]/a   全部城市a标签的层级关系
    li_list=tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    all_city_name=[]
    for li in li_list:
        city_name=li.xpath('./text()')[0]
        all_city_name.append(city_name)
    print(all_city_name,len(all_city_name))
