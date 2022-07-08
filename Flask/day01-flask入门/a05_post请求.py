# -*-coding:utf-8-*-
# Autor:编程的小姐姐
# DateTime:2022/4/18 21:38
# File:a05_post请求
from flask import Flask,request

app = Flask(__name__)


@app.route('/login',methods=["GET","POST"]) #，methods表示支持的请求，默认只支持get
def login():

    if request.method == "GET":
        return "GET请求"
    elif request.method == "POST":
        return "POST请求"



if __name__ == '__main__':
    app.run(debug=True)