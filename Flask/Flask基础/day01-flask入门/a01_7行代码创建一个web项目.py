# -*-coding:utf-8-*-
# Autor:编程的小姐姐
# DateTime:2022/4/18 20:34
# File:01-7行代码创建一个web项目

from flask import Flask
app = Flask(__name__,
            static_folder='aaa')
print(__name__)

@app.route('/')
def hello_world():
    return '欢迎来到羊驼老师的课堂'


if __name__ == '__main__':
    app.run(debug=True)