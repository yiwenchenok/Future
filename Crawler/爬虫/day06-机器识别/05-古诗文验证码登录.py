#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 05-古诗文验证码登录.py
import requests
from PIL import Image
from bs4 import BeautifulSoup
import pytesseract
import matplotlib.pyplot as mp #pip install matplotlib
# todo:保持会话访问
s = requests.Session()
# 验证码的地址
url_yzm = 'https://so.gushiwen.cn/RandCode.ashx'
# 获取登录页面地址
login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
# 构造请求头
header = {
    'referer': 'https://www.gushiwen.cn/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}
# 先请求登录地址
res = s.get(login_url, headers=header)
soup = BeautifulSoup(res.text,'lxml')
#todo: 获取隐藏域中令牌 __VIEWSTATEGENERATOR和__VIEWSTATE
__VIEWSTATEGENERATOR = soup.find("input",id='__VIEWSTATEGENERATOR')['value']
__VIEWSTATE = soup.find("input",id='__VIEWSTATE')['value']
# ，然后拿到验证码图片
res = s.get(url_yzm, headers=header)
with open('code.png', "wb") as f:
    f.write(res.content)  # 写入二进制流的图片
def rec_yzm():
    """识别不准，需要自己训练
    https://ai.baidu.com/easydl/
    """
    image = Image.open('code.png')
    mp.imshow(image)
    mp.show()
    # 灰化处理
    lim = image.convert("L")
    # 二值化处理
    xx = 160
    table = []
    for i in range(256):
        if i < xx:
            table.append(0)
        else:
            table.append(1)
    bim = lim.point(table, '1')
    text = pytesseract.image_to_string(bim, "chi_sim")
    return text[:4]
def rec_yzm_rengong():
    """人工之别"""
    image = Image.open('code.png')
    mp.imshow(image)
    mp.show()
    text = input("请输入您的验证码：")
    return text[:4]
# 识别验证码
code = rec_yzm_rengong()
print("识别结果：",code)
# 构造form数据
data = {
    "__VIEWSTATE": __VIEWSTATE,
    '__VIEWSTATEGENERATOR': __VIEWSTATEGENERATOR,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '13318011750',
    'pwd': '5560318abcd',
    'code': code,
    'denglu': '登录'
}
# 登录请求地址
post_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
#发送post请求
res = s.post(post_url,headers=header,data=data)
html = res.text
if "修改密码"  in html:
    print("登录成功")
    print(res.cookies)
else:
    print("登录失败")
