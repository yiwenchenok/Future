# -*-coding:utf-8-*-
# Autor:编程的小姐姐
# DateTime:2022/4/21 20:17
# File:01-abort
from flask import Flask,jsonify,render_template

app = Flask(__name__)

@app.route("/")
def index():
    # return 'ok','888',{'content-type':'text/html'}
    return render_template('index.html') #返回模板


@app.route("/js")
def js():
    st = {'a':1123,'b':456}
    res = jsonify(st)
    print(type(st)) ##<class 'dict'>
    print(type(res)) #<class 'flask.wrappers.Response'>
    return res


if __name__ == '__main__':
    app.run(debug=True)