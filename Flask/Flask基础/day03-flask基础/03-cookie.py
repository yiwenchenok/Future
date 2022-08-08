# -*-coding:utf-8-*-
# Autor:编程的小姐姐
# DateTime:2022/4/21 20:41
# File:03-cookie

import datetime
from flask import Flask,make_response,request

app = Flask(__name__)

@app.route('/set-cookie')
@app.route("/")
def index():
    response = make_response('ok')
    # response.set_cookie('name','yangtuio',max_age=5) #5秒超时
    response.set_cookie('name','yangtuio',expires=datetime.datetime(2022,4,22)) #设置超时时间撮
    response.set_cookie('name2','flask')

    return response


@app.route('/get-cookie')
def get_cookie():
    '''
    获取cookie
    :return:
    '''
    cookie = request.cookies
    name = cookie.get('name') if 'name' in cookie else ''
    name2 = cookie.get('name2')

    return name + name2
@app.route('/del-cookie')
def del_cookie():
    '''
    获取cookie
    :return:
    '''
    res = make_response('删除cookie')
    res.delete_cookie('name')

    return res



if __name__ == '__main__':
    app.run(debug=True)