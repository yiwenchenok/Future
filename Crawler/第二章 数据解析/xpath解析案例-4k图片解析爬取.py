import os.path
import pprint

from lxml import etree
import requests

if __name__ == "__main__":\
    #1、爬取页面源码数据
    url='https://pic.netbian.com/4kmeinv/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
    }

    response=requests.get(url=url,headers=headers)

    page_text=response.text

    tree=etree.HTML(page_text)
    li_list=tree.xpath('//ul[@class="clearfix"]/li')
    #创建一个文件夹
    if not os.path.exists('./picLibs'):
        os.mkdir('./picLibs')
    for li in li_list:
        img_src='https://pic.netbian.com'+li.xpath('./a/img/@src')[0]
        img_name=li.xpath('./a/img/@alt')[0]+'jpg'
        #通用处理中文乱码的解决方案
        img_name=img_name.encode('iso-8859-1').decode('gbk')
        #请求图片进行持久化存储
        img_data=requests.get(url=img_src,headers=headers).content
        img_path='picLibs/'+img_name
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print(img_name,"打印成功")
