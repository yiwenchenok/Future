# -*-coding:utf-8-*-
# Autor:编程的小姐姐
# DateTime:2022/4/18 20:55
# File:a02_flask配置


from flask import Flask

app1 = Flask(__name__)

class MyConfig:
    DEBUG = True  #配置必须要大写，小写不会生效
    A = "我是一个A"
    a = "我是一个a"

#通过类的方式加载配置
app1.config.from_object(MyConfig)

#通过文件的方式加载配置
app1.config.from_pyfile('settings.py')

@app1.route('/')
@app1.route('/index')
def index():
    print("A:",app1.config.get("A")) #能正确获取到
    print("a:",app1.config.get("a"))  #None
    print("NAME:",app1.config.get("NAME"))  #None
    print("AGE:",app1.config.get("AGE"))  #None
    return "okk"

if __name__ == '__main__':
    app1.run()