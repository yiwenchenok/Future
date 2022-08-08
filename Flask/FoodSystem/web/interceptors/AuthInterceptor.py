# -*- coding: utf-8 -*-
from application import app
from flask import request, g, redirect
from web.models.User import (User)
from common.libs.user.UserService import (UserService)
from common.libs.UrlManager import (UrlManager)
import re

"""网页拦截，确保登录状态才可以访问index"""
@app.before_request
def before_request():
    ignore_urls = app.config['IGNORE_URLS']  # 完全不查的地址，如静态页面，不用做拦截请求判定
    ignore_check_login_urls = app.config['IGNORE_CHECK_LOGIN_URLS']  # 登录本身不需要做拦截，否则一直在重定向
    path = request.path

    # 如果是静态文件就不要查询用户信息了
    pattern = re.compile('%s' % "|".join(ignore_check_login_urls))  # 通过%s的正则表达式匹配字符直到空字符为止，/user/login|/user/login
    if pattern.match(path):
        return
    if '/api' in path:  # api也不做拦截
        return
    user_info = check_login()
    # 修改密码优化，通过g变量获取当前用户登录状态
    g.current_user = None
    if user_info:
        g.current_user = user_info
    pattern = re.compile('%s' % "|".join(ignore_urls))  # 不做拦截的路由，通过%s的正则表达式匹配字符直到空字符为止，/static | /favicon.ico
    if pattern.match(path):
        return
    if not user_info:
        return redirect(UrlManager.buildUrl("/user/login"))

    return
'''
判断用户是否已经登录,将cookie值取出来判断，登录后一定设置了cookie，授权码+uid,
通过uid查询用户是否存在，存在就根据用户信息生成授权tokon，然后和浏览器中返回的cookie中#之前
的授权授权码进行对比，一致则表示登录成功。
'''
def check_login():
    cookies = request.cookies
    auth_cookie = cookies[app.config['AUTH_COOKIE_NAME']] if app.config['AUTH_COOKIE_NAME'] in cookies else None#获取cookie对象的名称
    if '/api' in request.path:
        app.logger.info(request.path)
        auth_cookie = request.headers.get("Authorization")#Authorization：微信小程序认证信息的token，放在头部里面，能够知道是哪个用户，类似于cookie信息
        app.logger.info(request.headers.get("Authorization"))
    if auth_cookie is None:
        return False
    auth_info = auth_cookie.split("#")
    if len(auth_info) != 2:
        return False
    try:
        user_info = User.query.filter_by(uid=auth_info[1]).first()#获取cookies里面的id，并且返回该用户的信息
    except Exception:
        return False
    if user_info is None:#用户不存在，返回登录界面
        return False
    #geneAuthCode(user_info)：cookie生成方法，以用户的id，登录名，密码，和用户绑定的随机生成的16位字符串进行的哈希编码的结果
    if auth_info[0] != UserService.geneAuthCode(user_info):#用户登录生成的cookie和最新cookie不一致，返回登录界面：比如修改了密码
        return False
    if user_info.status != 1:  # todo:删除一个账号后，立即会进行退出操作，否则删除之后没有退出
        return False
    return user_info
