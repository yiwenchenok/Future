
# File:01-abort about函数的作用是：放弃请求并返回错误代码

from flask import Flask,abort
app = Flask(__name__)

@app.route("/<flag>")
def index(flag):
    if flag == "del":
        abort(404)  #抛出一个404错误
    return 'ok'
#重造404页面
# @app.errorhandler(404)
# def eror404(e):
#     return '你的请求不合法；404:'+str(e)

if __name__ == '__main__':
    app.run(debug=True)