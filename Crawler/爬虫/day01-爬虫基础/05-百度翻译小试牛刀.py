#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 05-百度翻译小试牛刀.py
import urllib.request
import urllib.parse

# 请求路由
# url = "https://fanyi.baidu.com/langdetect"
url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"

# 构造headers
header = {
    "Host": "fanyi.baidu.com",
    "Origin": "https://fanyi.baidu.com",
    "Referer": "https://fanyi.baidu.com/?aldtype=16047",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Cookie": "BAIDUID=E16E09550B6B74C111D6C54EECD5264E:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1652602619; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1652602619; ab_sr=1.0.1_ZmY3ZjAwYjBjYmY5ZjYyODJkOWIyYjQ2NGFlZDJiZDkxNGIxZDI3YThjYjZiZTI3YzdkMzhiZjNkYjE3MGM2YzE5MzI0OGY1N2VhNjI5NDFjOGY2M2M2ZjM5MjIxMGE5ZDZjZTkwZGI5YjMzMzgxOTJiNGIzMGVkMGEwNjVlYzViNzBlNTUwODZjMTE1YmNkNzZkNGQwYjU2YjBlN2NkYQ=="
}

# 构造请求参数
form_data = {
    "from": "en",
    "to": "zh",
    "query": "python",
    "transtype": "translang",
    "simple_means_flag": 3,
    "sign": "477811.239938",
    "token": "7355646b3194a5a7589a774b689bef83",
    "domain": "common"
}
#urllib需要转，request不用
# 将请求参数转成字节类型
form_data = bytes(urllib.parse.urlencode(form_data), encoding='utf-8')
# 构造请求对象
request = urllib.request.Request(url=url, data=form_data, headers=header)
# 发送请求  传了data就表示是一个post请求
res = urllib.request.urlopen(request)
print(res.read().decode())
