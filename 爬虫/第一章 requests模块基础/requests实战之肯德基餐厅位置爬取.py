import requests
import pprint
import json
if __name__=='__main__':
    # 1.指定url
    url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    # 2.post请求数据封装字典
    kw=input('请输入你需要查询的肯德基餐厅位置地址:')
    data={
    'cname':'',
    'pid':'',
    'keyword': kw,
    'pageIndex': '1',
    'pageSize': '10',
    }
    # 3.进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
    }
    # 4.发送请求
    response = requests.post(url=url,data=data,headers=headers)
    # 5.存储
    list_data=response.json()
    pprint.pprint(list_data)
    fp = open('data/'+kw+'kfc.json', 'w', encoding='utf-8')
    json.dump(list_data, fp=fp, ensure_ascii=False)
    print('成功')