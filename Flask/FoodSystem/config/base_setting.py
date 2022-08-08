# -*- coding: utf-8 -*-
SERVER_PORT = 8999
DEBUG = False
SQLALCHEMY_ECHO = False

# 有可能你使用浏览器看到的一串字符串不是那么容易看懂的，这是因为python底层使用unicode编码。
# 通过设置下面的参数可以解决这个问题。
JSON_AS_ASCII = False

AUTH_COOKIE_NAME = "FoodSystem"  # config中设置cookie对象的名称用法，response.set_cookie( app.config['AUTH_COOKIE_NAME']
SEO_TITLE = "Python Flask微信小程序订餐系统"

# todo:在web/interceptors/AuthInterceptor.py中before_request中使用过滤，登录中的逻辑
# 过滤的url
IGNORE_URLS = [
    "^/user/login"
]
# 完全不用判断登录状态的，/static
IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]

API_IGNORE_URLS = [
    "^/api"
]


PAGE_SIZE = 50  # 分页的个数
PAGE_DISPLAY = 10  # 演示多少页

STATUS_MAPPING = {
    "1": "正常",
    "0": "已删除"
}

UPLOAD = {
    'ext': ['jpg', 'gif', 'bmp', 'jpeg', 'png'], #上传图片规定的格式
    'prefix_path': '/web/static/upload/',#上传图片的路径
    'prefix_url': '/static/upload/'#上传图片的路由
}
#用来指定端口
APP = {
    'domain': 'http://127.0.0.1:8999' #
}

MINA_APP = {
    'appid': 'wx9fcb94eea918a33c',
    'appkey': '14a8bd65fb849774d1650483d0409a96',
    'paykey': 'xxxxxxxxxxxxxx换自己的',
    'mch_id': 'xxxxxxxxxxxx换自己的',
    'callback_url': '/api/order/callback'
}

PAY_STATUS_MAPPING = {
    "1": "已支付",
    "-8": "待支付",
    "0": "已关闭"
}

PAY_STATUS_DISPLAY_MAPPING = {
    "0": "订单关闭",
    "1": "支付成功",
    "-8": "待支付",
    "-7": "待发货",
    "-6": "待确认",
    "-5": "待评价"
}
