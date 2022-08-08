
# File:03-动态路由
from flask import Flask
app = Flask(__name__)

@app.route('/index/<id>')
def index(id):
    return f"获取的参数为：{id}"

# 默认<>的规则匹配不带/的整数
@app.route('/param_int/<int:id>')
def get_url_param_int(id):
    return f'获取的参数是：{id}'


# 默认<>的规则匹配不带/的整数
@app.route('/param_float/<float:id>')
def get_url_param_float(id):
    return f'获取的参数是：{id}'


# 匹配参数后面带/
@app.route('/param_path/<path:p>')
def get_url_param_path(p):
    return '获取的参数是： %s '% p

if __name__ == '__main__':
    app.run(debug=True)