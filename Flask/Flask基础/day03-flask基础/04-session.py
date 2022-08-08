# -*-coding:utf-8-*-
# Autor:编程的小姐姐
# DateTime:2022/4/21 21:21
# File:04-session

from flask import Flask, session,jsonify
import datetime


class Config():
    SECRET_KEY = "lkadjglkA4dfalkjakgjklag656523989##^^?"


app = Flask(__name__)
app.config.from_object(Config)
# app.config["SECRET_KEY"] = "lkadjglk4656523989##^^?"

@app.route("/set-session")
def index():
    """
    设置session
    :return:
    """
    #todo:设置session超时
    session.permanent = True #开启
    app.permanent_session_lifetime = datetime.timedelta(seconds=5) #设置超时为5秒
    # app.permanent_session_lifetime = datetime.timedelta(days=7) #设置超时为7天


    session["name"] = "python"
    session["user_id"] = 1



    return "ok"



@app.route("/get-session")
def get_session():
    """
    获取session
    :return:
    """
    dic = {}
    dic["name"] = session.get('name')
    dic["user_id"] = session.get('user_id')
    dic["age"] = session.get('age')




    return jsonify(dic)


@app.route("/del-session")
def del_sesson():
    """
    删除session
    :return:
    """
    # name = session.pop('name') if 'name' in session.keys() else "" #删除并返回删除的session的值
    # return f"删除:{name}"

    session.clear() #清空所有的session

    return "ok"





if __name__ == '__main__':
    app.run(debug=True)
