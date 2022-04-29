#需求：爬取三国演义小说所有的章节标题和章节内容
import pprint

from bs4 import BeautifulSoup
import requests
if __name__ == "__main__":
    url_link=[]
    url='https://www.shicimingju.com/book/sanguoyanyi.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
    }
    response=requests.get(url=url,headers=headers)
    response.encoding='utf-8'
    page_text=response.text
    soup = BeautifulSoup(page_text, 'lxml')
    li_list=soup.select('.book-mulu> ul >li')
    fp =open('./sangou.txt','w',encoding='utf-8')
    for li in li_list:
        title= li.a.string
        detail_url='https://www.shicimingju.com'+li.a['href']
        #对详情页发起请求，解析出章节内容
        detail_page_text=requests.get(url=detail_url,headers=headers).text
        #解析出详情页中相关的章节内容
        detail_soup=BeautifulSoup(detail_page_text,'lxml')
        div_tag=detail_soup.find('div',class_='chapter_content')
        #解析到了章节的内容
        content=div_tag.text
        fp.write(title+':'+content+'\n')
        print(title,'爬取成功')




