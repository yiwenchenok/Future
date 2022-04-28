import json
import pprint

import requests
if __name__=='__main__':
    # 1.指定url
    post_url='https://fanyi.baidu.com/sug'
    # 2.进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
    }
    # post请求参数处理(同get请求一致)
    kw = input('输入搜索关键字:')
    data = {
        'kw':kw
    }
    # 4.请求发送
    response=requests.post(url=post_url,data=data,headers=headers)
    # 5.获取响应数据:json()方法返回的是obj(如果确定响应数据是json类型,才可以使用json() )
    dic_obj=response.json()
    pprint.pprint(dic_obj)
    filename=kw+'.json'
    fp = open('./data/'+filename,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)
    print('成功')
