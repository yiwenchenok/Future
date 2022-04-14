import requests
from bs4 import BeautifulSoup
import translation as t
from my_sqlite import *

#打开网址，获取源码
def open_url(url):
    headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 SE 2.X MetaSr 1.0",
    }
    req = requests.get(url,headers=headers)
    #设置网页编码格式
    req.encoding = req.apparent_encoding
    
    return req.text

def get_url(res):
    #将网页源码转换成标签树形式
    soup = BeautifulSoup(res, "lxml")
    #查找h3标签且class是"gc__title"的标签
    source = soup.find_all('h3',class_="gc__title")
    result = []
    for each in source:
        result.append([each.a['href'],t.translate(each.span.text)])

    return result
    """
    temp = soup.find_all('div',class_="gc__excerpt")
    for each in temp:
        print(t.translate(each.p.text))
    """

def main():
    create_table()
    url = 'https://www.aljazeera.net/search/china'
    res = open_url(url)
    result = get_url(res)
    try:
        connect()
    except:
        pass
    try:
        create_table()
    except:
        pass
    insert(result)

if __name__ == "__main__":
    main()
