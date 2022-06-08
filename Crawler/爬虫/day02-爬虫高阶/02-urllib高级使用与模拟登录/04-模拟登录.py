#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Lama Pocos
# @email  : 249084156@qq.com
# @File desc  : 04-模拟登录.py

import urllib.request
import re
import http.cookiejar
import urllib.parse

class LoginZhiWang():
    def __init__(self):
        cookie = http.cookiejar.LWPCookieJar() #创建保存cookie的对象
        #创建cookie_handleer
        cookie_hander = urllib.request.HTTPCookieProcessor(cookie)

        #创建opner
        self.opener = urllib.request.build_opener(cookie_hander)

        self.header = {
            'Host': 'login.cnki.net',
            'Referer': 'https://login.cnki.net/?returnurl=https%3a%2f%2fwww.cnki.net',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
            'Cookie': 'Ecp_ClientId=2210326112701958919; cnkiUserKey=0474120c-fca1-fb11-ab87-71d786657c68; Ecp_loginuserjf=249084156@qq.com; Ecp_Userid=1001606383; UM_distinctid=17a79989095482-0a0deb48d3105a-6373267-1fa400-17a799890965c1; Ecp_ClientIp=223.74.64.35; SID=020132; _pk_ref=%5B%22%22%2C%22%22%2C1628600095%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DskV6my7RrPcGXQglkDE30xeujezylEIW0MtSaMEnrXG%26wd%3D%26eqid%3Dbfffc27d000220f20000000661127717%22%5D; _pk_id=c44a9094-6725-4037-8e38-2ec0bd90d531.1616729274.7.1628600095.1628600095.; _pk_ses=*; ASP.NET_SessionId=nzr0rbwrsotip4ce1llbsa5b; Ecp_IpLoginFail=210810223.74.64.206'
        }



    def get_param(self):
        """
        获取隐藏域实时的参数
        :return:
        """

        url = 'https://login.cnki.net/?returnurl=https%3a%2f%2fwww.cnki.net'


        # 构造请求对象
        reque = urllib.request.Request(url, headers=self.header)
        # response = urllib.request.urlopen(reque) #发送get请求
        response = self.opener.open(reque) #发送get请求 todo:用同一个opener
        html = response.read().decode()

        __VIEWSTATE = re.findall('id="__VIEWSTATE" value="(.*?)"',html)[0]
        __VIEWSTATEGENERATOR = re.findall('id="__VIEWSTATEGENERATOR" value="(.*?)"',html)[0]
        __EVENTVALIDATION = re.findall('id="__EVENTVALIDATION" value="(.*?)"',html)[0]
        __EVENTTARGET ='Button1'
        __EVENTARGUMENT = ''
        TextBoxUserName='249084156@qq.com'
        TextBoxPwd = 'admin123456'
        CheckBoxAutoLogin= 'on'
        ecpuip = '223.74.64.206'

        form_data = {
            '__VIEWSTATE':__VIEWSTATE,
            '__VIEWSTATEGENERATOR':__VIEWSTATEGENERATOR,
            '__EVENTVALIDATION':__EVENTVALIDATION,
            '__EVENTTARGET':__EVENTTARGET,
            '__EVENTARGUMENT':__EVENTARGUMENT,
            'TextBoxUserName':TextBoxUserName,
            'TextBoxPwd':TextBoxPwd,
            'CheckBoxAutoLogin':CheckBoxAutoLogin,
            'ecpuip':ecpuip,
        }

        return form_data

    def login(self):
        form_data = self.get_param()
        # 将请求参数构造成字节类型
        form_data = bytes(urllib.parse.urlencode(form_data), encoding='utf-8')

        # post请求的地址
        url = 'https://login.cnki.net/?returnurl=https%3a%2f%2fwww.cnki.net'

        # 加一个data参数就是发送post请求
        reque = urllib.request.Request(url, headers=self.header,data=form_data)
        response = self.opener.open(reque) #发送post请求  todo:用同一个opener


        res = self.opener.open('https://www.cnki.net/?UID=WEEvREcwSlJHSldTTEYzVnBFbFF5NVVWY2xBZ3MyWTZrdkJodzBubHdOMD0%3d%249A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&PlatForm=')
        html = res.read().decode()
        print(html)
        if re.search('249084156@qq.com',html):
            print("登录成功")
        else:
            print('登录失败')



if __name__ == '__main__':
    g = LoginZhiWang()
    g.login()
