import pprint

from lxml import etree
import requests

#爬取58二手房中的房源信息
if __name__ == "__main__":\
    #1、爬取页面源码数据
    url='https://anqiu.58.com/ershoufang/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
    }
    page_text=requests.get(url=url,headers=headers).text
    # pprint.pprint(page_text)
    #2.xpath路径解析
    tree = etree.HTML(page_text)
    li_list=tree.xpath('//section[@class="list"]/div')
    #3.持续化存储
    fp=open('58.txt','w',encoding='utf-8')
    for li in li_list:
        title=li.xpath('./a/div[2]//div/h3/text()')[0]
        link=li.xpath('./a/@href')[0]
        print(title)
        print(link)
        fp.write(title+'\n'+link)
