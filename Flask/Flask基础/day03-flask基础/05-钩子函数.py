# -*-coding:utf-8-*-
# Autor:编程的小姐姐
# DateTime:2022/4/21 21:49
# File:05-钩子函数

from flask import Flask, abort
import datetime

app = Flask( __name__ )

# 只有在第一次请求的时候执行
@app.before_first_request
def first_request():
    print("before_first_request 执行")


# 每次请求之前执行
@app.before_request
def before_request_():
    print('before_request执行') # 每次执行完成后没有未处理的异常抛出才会执行


@app.before_request
def before_request_2():
    print('before_request2执行')  # 每次执行完成后没有未处理的异常抛出才会执行


@app.after_request
def after_request(response):
    print('after_request 执行')
    return response


@app.teardown_request
def teardown_request_(response):
    print('teardown_request 执行')
    return response

@app.route('/')
def index():
    print('index 执行')
    return 'ok'


if __name__ == '__main__':
    # Flask 应用程序实例的方法run启动web服务器
    app.run(debug=True)