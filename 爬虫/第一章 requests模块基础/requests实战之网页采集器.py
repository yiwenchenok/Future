import pprint
import requests

# UA:User-Aagent(请求载体的身份标识)
# UA伪装:门户网站的服务器会检测对应的请求的载体身份标识,如果检测到请求的载体身份标识为某一款浏览器,说明该请求是一个正常请求
# 但是,如果检测到请求的载体身份标识不是基于某一款浏览器的则表示改请求为不正常的请求(爬虫),则服务器端就很有可能拒绝该次请求

# UA伪装:让爬虫对应的请求载体身份标识伪装成某一款浏览器
if __name__ == '__main__':
    # UA伪装:将对应的User-Agent封装到一个字典中

    url = 'https://www.sogou.com/web'
    # 处理url携带的参数:封装到字典中
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
    }
    kw=input('输入搜索关键字:')
    param ={
        'query':kw
    }
    # 对指定的url放弃的请求对应的url是携带参数的,并且请求过程中处理了参数
    response=requests.get(url=url,params=param,headers=headers)
    page_text=response.text
    fileName=kw+'.html'
    pprint.pprint(page_text)
    with open(fileName,'w',encoding='utf-8')as fp:
        fp.write(page_text)
    print(fileName,'保存成功')