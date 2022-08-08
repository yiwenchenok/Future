# -*- coding: utf-8 -*-
from application import app
from flask import request,g,jsonify
from web.models.member.Member import Member
from common.libs.member.MemberService import MemberService
import  re


'''
api认证
'''

@app.before_request
def before_request_api():
    api_ignore_urls = app.config['API_IGNORE_URLS']  #小程序端主页是不需要做拦截的 API_IGNORE_URLS = [ "^/api"]
    path = request.path
    if '/api' not in path: #只处理/api的接口，没有api不做拦截处理
        return
    # 能否拿到Authorization验证小程序中是否登录，没有登录则返回False,反之返回这个用户信息实例
    member_info = check_member_login()
    g.member_info = None  #通过g变量获取当前用户登录信息，先将全局的这个设置为空
    if member_info:
        g.member_info = member_info #如果有信息，则将此用户信息设置为全局
    pattern = re.compile('%s' % "|".join( api_ignore_urls ))  #不登录也可以访问的页面，不需要做拦截
    if pattern.match(path):
        return
    if not member_info : #todo:如果用户信息不存在，则返回错误json，相当于拦截了请求
        resp = {'code': -1, 'msg': '未登录呀~', 'data': {}}
        return jsonify(resp)
    return  #不做拦截

'''
判断用户是否已经登录
'''
def check_member_login():
    #print(request.headers)
    '''
    Host: 127.0.0.1:8999
    Connection: keep-alive
    Content-Length: 37
    Authorization: 8b15f29b49b76a3cb36a08754225a904#9
    User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1 wechatdevtools/1.06.2208010 MicroMessenger/8.0.5 webview/
    Content-Type: application/x-www-form-urlencoded
    Accept: */*
    Sec-Fetch-Site: same-site
    Sec-Fetch-Mode: cors
    Sec-Fetch-Dest: empty
    Referer: https://servicewechat.com/wx9fcb94eea918a33c/devtools/page-frame.html
    Accept-Encoding: gzip, deflate, br
    '''
    auth_cookie = request.headers.get("Authorization")  #小程序发送请求中的头部信息是否有Authorization，类似于cookie的功能
    if auth_cookie is None:
        return False
    auth_info = auth_cookie.split("#")  #通过#拼接的token在保存到数据库时已经保存了
    if len(auth_info) != 2: #表示没有token信息
        return False
    try:   #数据库存储的信息校对小程序中的token Authorization
        member_info = Member.query.filter_by(id=auth_info[1]).first()
    except Exception:
        return False
    if member_info is None:
        return False
    if auth_info[0] != MemberService.geneAuthCode(member_info):  #授权码验证
        return False
    if member_info.status != 1: #用户信息无效
        return False
    return member_info #验证通过就返回用户信息的实例

