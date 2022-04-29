import pprint

import requests
if __name__ == '__main__':
    # step_1:指定url
    url='https://www.sogou.com/'
    # step_2:发起请求
    # get方法会返回一个响应对象
    response = requests.get(url)
    # step_3:获取响应数据.text返回的是字符串形式的响应数据
    page_text=response.text
    pprint.pprint(page_text)
    with open('data/sogou.html', 'w', encoding='utf-8')as fp:
        fp.write(page_text)
    print('爬取数据结束')

