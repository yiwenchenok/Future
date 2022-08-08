# -*-coding:utf-8-*-
# Autor:编程的小姐姐
# DateTime:2022/4/25 21:24
# File:02-特殊变量
from flask import Flask ,flash,render_template,session


app= Flask(__name__)

app.config["SECRET_KEY"] = 'adjglkajdglkaj'
app.config["DESC"] = '帅气的羊驼老师'

@app.route("/")
def flash_():

    #flash特殊变量
    flash('python')
    flash('django')

    #session
    session["username"] = "不掉发的羊驼老师"

    return render_template('flash.html')

@app.route("/index")
def index():
    return 'index'

if __name__ == '__main__':
    app.run(debug=True)