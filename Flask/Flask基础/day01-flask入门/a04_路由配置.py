# -*-coding:utf-8-*-
# Autor:编程的小姐姐
# DateTime:2022/4/18 21:24
# File:a03_路由配置
from flask import Flask

app = Flask(__name__)


"""
同一个路由装饰不同的视图函数：匹配第一个
同一个视图函数有多个路由装饰：都生效

路： 广州 > 北京   坐飞机  坐船  坐火车  三条路到达同一个终点可不可以？ 当然可以
     京广GZ0500 可以从北京 到广州 ，可不可以从北京到乌鲁木齐? 不行 一条路只能有一个终点（视图）
"""


@app.route("/index1")
@app.route('/index')
def index1():
    return 'index1'#index1生效


@app.route('/index')
def index2():
    return 'index2'








if __name__ == '__main__':
    print(app.url_map)  #查看所有路由
    app.run(debug=True)