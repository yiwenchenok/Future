# -*-coding:utf-8-*-
# Autor:编程的小姐姐
# DateTime:2022/4/18 21:24
# File:a03_路由配置
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "ok"

def index1():
    return "ok22222"

#另外一种路由配置方式，不推荐
app.add_url_rule("/index",endpoint="index1",view_func=index1)

if __name__ == '__main__':
    print(app.url_map)  #查看所有路由
    app.run(debug=True)