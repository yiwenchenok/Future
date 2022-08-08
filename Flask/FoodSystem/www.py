# -*- coding: utf-8 -*-

from application import app
from web.views.index import route_index
from web.views.static import route_static
from web.views.user.User import route_user
from web.views.account.Account import route_account
from web.views.upload.Upload import route_upload
from web.views.api import route_api
from web.views.member.Member import route_member
from web.views.food.Food import route_food
from web.views.finance.Finance import route_finance
from web.views.stat.Stat import route_stat
from web.views.chart import route_chart

'''
统一拦截处理和统一错误处理
'''
from web.interceptors.ApiAuthInterceptor import *
from web.interceptors.AuthInterceptor import *
from web.interceptors.ErrorInterceptor import *

'''
蓝图功能，对所有的url进行蓝图功能配置
'''
app.register_blueprint(route_index, url_prefix="/")
app.register_blueprint(route_user, url_prefix="/user")
app.register_blueprint(route_static, url_prefix="/static")
app.register_blueprint(route_account, url_prefix="/account")
app.register_blueprint(route_food, url_prefix="/food")
app.register_blueprint(route_upload, url_prefix="/upload")
app.register_blueprint(route_api, url_prefix="/api")
app.register_blueprint(route_member, url_prefix="/member")
app.register_blueprint(route_finance, url_prefix="/finance")
app.register_blueprint(route_stat, url_prefix="/stat")
app.register_blueprint(route_chart, url_prefix="/chart")
