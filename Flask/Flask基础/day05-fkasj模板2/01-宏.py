# -*-coding:utf-8-*-
# Autor:编程的小姐姐
# DateTime:2022/4/25 20:27
# File:01-宏

from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register")
def register():
    return render_template("register.html",name="欢迎来到羊驼老师的课堂")

if __name__ == '__main__':
    app.run(debug=True)