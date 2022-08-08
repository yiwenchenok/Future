#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/6 20:15
# @Author  : 羊驼
# @File    : 01-邮件扩展.py
# @Software: PyCharm
'''
ITWNBLHBZIWWOIAY
SMTP服务器: smtp.163.com
'''

from flask import Flask
from flask_mail import Mail,Message

app = Flask(__name__)


class Config:
    MAIL_SERVER = "smtp.qq.com"  #邮箱地址
    MAIL_PORT = 25 #smtp端口
    MAIL_USE_TLS = True #使用tls安全协议
    MAIL_USERNAME = "1820312463@qq.com" #邮箱地址
    MAIL_PASSWORD = "zapgenybpxdibccf" #客户端授权码

app.config.from_object(Config)


#邮件连接
mail = Mail(app)


@app.route("/")
def index():
    """发送邮件"""
    #1.构造邮件对象
    # subject 邮件标题
    # sender 发送方
    # recipients 接收方列表，如果多个接收方，那么是群发。
    # cc 抄送列表
    # bcc 密件抄送
    # attachments 附件实例列表
    # body 邮件文本正文
    # html 网页形式的正文
    msg = Message(
        subject="这是羊驼老师的课堂测试~",
        sender = app.config.get("MAIL_USERNAME"),
        recipients = ["978506662@qq.com","1820312463@qq.com"],
        cc = "1820312463@qq.com",
        body = "欢迎来到羊驼老师的课堂，这是一次发送邮件的课，希望大家喜欢",
        # html = "<h1>我在学习flask</h1>"
    )
    #2.添加附件
    msg.attach("黄图.jpg",content_type="image/jpeg",data=open("黄图.jpg",'rb').read())

    #3.发送邮件
    mail.send(msg)

    return "发送成功"


if __name__ == '__main__':
    app.run(debug=True)