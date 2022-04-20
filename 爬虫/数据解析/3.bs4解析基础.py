import pprint

from bs4 import BeautifulSoup

if __name__=='__main__':
    fp=open('./data/test.html','r',encoding='utf-8')
    # lxml bs4固定数据解析器
    soup=BeautifulSoup(fp,'lxml')
    # print(soup)
    # print(soup.a) soup.tagName 返回的是html中第一次出现的tagName标签
    # print(soup.find('div')) #find(tagName):等同于soup.tagName
    # print(soup.find('div',class_='song'))
    pprint.pprint(soup.find_all('a'))