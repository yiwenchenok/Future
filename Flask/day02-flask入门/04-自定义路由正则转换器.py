# -*-coding:utf-8-*-
# Autor:编程的小姐姐
# DateTime:2022/4/19 20:38
# File:04-自定义路由正则转换器
from flask import Flask,url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)

class RegexConverter(BaseConverter):
    def __init__(self,url_map,*args):
        super(RegexConverter,self).__init__(url_map)# 调用父类的初始化方法
        print(args[0])  # \d{3}
        self.regex = args[0] # 将正则表达式传给转换器对象，flask在解析路径的时候，会来这里获取regex保存的正则表达式
    def to_python(self, value):
        print(f"to_python中获取的value:{value}") #动态路由中的参数value进行处理
        return value
    def to_url(self, value):
        # 当使用反解析的时候会调用这个方法,可以对动态路由中的参数value进行处理
        print(f'反向解析的时候调用：{value}')
        return value


#注册正则转换器
app.url_map.converters["re"] = RegexConverter


@app.route("/index/<re('\d{3}'):page>")
def index(page):
    return f"获取的参数：{page}"

@app.route("/hello")
def hello():
    return url_for('index',page="123") #反向解析

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)