# -*-coding:utf-8-*-
# Autor:编程的小姐姐
# DateTime:2022/4/22 20:52
# File:02-模板

from flask import Flask,render_template

app = Flask(__name__)


def filter_mod_1(num):
    return num % 2
# 该方法第一个参数是函数名，第二个参数是自定义的过滤器名称。
app.add_template_filter(filter_mod_1, 'filter_my')

@app.template_filter("cut_list")
def cut_list(lis,start,end):
    return lis[start:end]


@app.route("/")
def index():
    dic = {
        'name':'羊驼afdsjlkdajglkjdalskjgdas;kljgklajgklagj',
        'age':18,
        'html':'<script>alert("你这个逗比")</script>'
    }
    return render_template('index.html',**dic)




if __name__ == '__main__':
    app.run(debug=True)