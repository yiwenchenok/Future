


# File:02-反向解析
#url_for 可以通过视图函数名称，反向解析得到视图对应的url.
from flask import Flask,url_for,redirect
app = Flask(__name__)
@app.route("/indexxxx")
def index():
    return "index"
@app.route("/hello")
def hello():
    # return url_for('index') #url_for通过endpoint反向解析出url的字符串  /indexxxx
    return redirect(url_for('index')) #重定向到/indexxxx
if __name__ == '__main__':
    print(app.url_map)
    app.run(port="8888",debug=True)