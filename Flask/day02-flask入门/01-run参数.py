
# File:01-run参数


from flask import Flask,current_app
class Config:
    A = "欢迎来到羊驼老师的课堂"

app = Flask(__name__)
#设置配置信息获取方式，从配置对象中查找
app.config.from_object(Config)

@app.route("/")
def index():
    #第一种方式：在能访问到app对象的文件中可直接使用app.config.get方法获取配置参数
    print(app.config.get("A")) #获取配置信息
    #第二种方式：需要从flask中导入current_app，在整个Flask项目中都可以使用，实际上也是app对象相到于一个别名.
    print(current_app.config.get("A")) #效果同上
    return "欢迎来到羊驼老师的课堂"


if __name__ == '__main__':
    print(app.url_map)  #查看路由信息
    app.run(host='0.0.0.0',port="8888",debug=True)

    '''
    host            服务器主机地址，默认使用本机地址'127.0.0.1'
    port            端口号,默认5000
    debug           参数是bool值 ,表示是否开启调试，True开启调试。默认Flase
    '''