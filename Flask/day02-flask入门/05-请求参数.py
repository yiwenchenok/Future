
# File:05-请求参数
from flask import Flask,request


app = Flask(__name__)

@app.route("/index",methods=['get','post'])
def index():
    print("request.args：",request.args)
    # print(request.args.getlist('name'))  #获取一键多值
    print(request.args.get("name"))

    print("request.form:",request.form)
    print(request.form.get("name"))

    print("request.values:", request.values)
    print(request.values.getlist("name"))

    # print("request.headers:", request.headers)
    print(request.headers.get("Host"))

    return "ok"


if __name__ == '__main__':
    app.run(debug=True)