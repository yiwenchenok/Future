# -*-coding:utf-8-*-
# Autor:编程的小姐姐
# DateTime:2022/4/22 20:43
# File:01-g对象
from flask import Flask, g
import datetime

app = Flask( __name__ )

# 每次请求之前执行
@app.before_request
def before_request_():
    g.username = "不掉发的羊驼老师"
    g.desc = "欢迎来到羊驼老师的课堂"
    print('before_request执行') # 每次执行完成后没有未处理的异常抛出才会执行



@app.route('/')
def index():
    print(g.get('username'))
    print(g.get('desc'))
    return 'ok'


if __name__ == '__main__':
    # Flask 应用程序实例的方法run启动web服务器
    app.run(debug=True)