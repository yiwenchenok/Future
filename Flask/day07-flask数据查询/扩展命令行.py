# -*-coding:utf-8-*-
# Autor:编程的小姐姐
# DateTime:2022/4/28 22:13
# File:扩展命令行
from flask import Flask
from flask_script import Manager

app = Flask(__name__)


manage = Manager(app)

@app.route("/")
def index():
    return "ok"


if __name__ == '__main__':
    # app.run(debug=True)
    manage.run()