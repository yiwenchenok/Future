import json

import requests
import pprint

if __name__=='__main__':
     # 1.指定url
     url='https://movie.douban.com/j/chart/top_list'
     # 2.条件字典封装
     param={
          'type': '24',
          'interval_id': '100:90',
          'action': '',
          'start': '1',
          'limit': '20',
     }
     # 3.进行UA伪装
     headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
     }
     # 4.请求发送
     response = requests.get(url=url, params=param, headers=headers)
     list_data=response.json()
     pprint.pprint(list_data)
     fp = open('data/douban.json', 'w', encoding='utf-8')
     json.dump(list_data, fp=fp, ensure_ascii=False)
     print('成功')
