import os.path
import pprint

from lxml import etree
import requests

if __name__ == "__main__":
    #1、爬取页面源码数据
    url='https://sc.chinaz.com/jianli/free.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
    }
    response=requests.get(url=url,headers=headers)
    response.encoding='utf-8'
    page_text=response.text
    tree=etree.HTML(page_text)
    if not os.path.exists('./jianLi'):
        os.mkdir('./jianLi')
    html_list=tree.xpath('//div[@id="container"]//p')
    print(html_list)
    alt_list = tree.xpath('.//div[@id="container"]/div')
    print(alt_list)
    for html in html_list:
        jianLi_list = 'https:' + html.xpath('./a/@href')[0]
        # print(jianLi_list)
        html_text = requests.get(url=jianLi_list,headers=headers).text
        tree = etree.HTML(html_text)
        down_url = tree.xpath('//div[@id="down"]/div[2]//li[1]/a/@href')[0]
        # print(down_url)
        down_name = tree.xpath('//div[@class="sc_warp clearfix"]/div[1]/a[3]')
        for name in down_name:
            jianLi_name = name.xpath('./text()')[0]
            jianLi_name = jianLi_name.encode('iso-8859-1').decode('utf-8')
            # print(jianLi_name)
            jianLi_path = 'jianLi/' + jianLi_name + '.rar'
            jianLi_data = requests.get(url=down_url,headers=headers).content
            with open(jianLi_path, 'wb') as fp:
                fp.write(jianLi_data)
                print(jianLi_name, '下载成功')


