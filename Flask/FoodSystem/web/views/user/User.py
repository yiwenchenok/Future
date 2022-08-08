# -*- coding: utf-8 -*-
from flask import Blueprint,render_template,request
from flask import Blueprint,request,jsonify,make_response,g,redirect
from web.models.User import ( User )
from common.libs.user.UserService import ( UserService )
from common.libs.Helper import ( my_render_template )
from common.libs.UrlManager import ( UrlManager )
from application import app,db
import json
route_user = Blueprint( 'user_page',__name__ )

@route_user.route( "/login",methods = [ "GET","POST" ] )
def login():
    if request.method == "GET":

        ############这个刚开始逻辑的时候没有，用于修改密码后，
        #在拦截器中使用g变量获取登录状态，如果获取到状态，表示
        if g.current_user:
            return  redirect( UrlManager.buildUrl("/") )
        ###############
        return my_render_template( "user/login.html" )  #返回页面

    resp = {'code': 200, 'msg': '登录成功~~', 'data': {}}
    req = request.values
    login_name = req['login_name'] if 'login_name' in req else ''
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ''

    if  login_name is None or len( login_name ) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入正确的登录用户名~~"
        return jsonify( resp )

    if  login_pwd is None or len( login_pwd ) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入正确的邮箱密码~~"
        return jsonify(resp)

    user_info = User.query.filter_by( login_name = login_name ).first()
    if not user_info:
        resp['code'] = -1
        resp['msg'] = "请输入正确的登录用户名和密码-1~~"
        return jsonify(resp)


    #todo:这里使用了写在通用里面的一个密码生成方法：用户设置的密码+随机生成的salt(密钥)算法进行加密后与数据库中对比
    # 一起组成的字符串案后md5加密,里面对密码encode使用了base64
    if user_info.login_pwd != UserService.genePwd( login_pwd,user_info.login_salt ):
        resp['code'] = -1
        resp['msg'] = "请输入正确的登录用户名和密码-2~~"
        return jsonify(resp)

    if user_info.status != 1:  #todo:已经被删除的账号，其字段status不为1的时候
        resp['code'] = -1
        resp['msg'] = "账号已被禁用，请联系管理员处理~~"
        return jsonify(resp)


    #todo：记录登录状态，写道cookie里面去，保证cookie安装，使用授权torkon的概念，cookie由两部分构成
    #通过#进行分割
    # 第一部分是UserService.geneAuthCode(user_info)：
    # 这个授权token,UserService.geneAuthCode(user_info)其实就是"uid-name-pwd-salt"组成字符串然后通过md5加密后组成，uid是字段主键primary key
    response = make_response(json.dumps({'code': 200, 'msg': '登录成功~~'}))
    response.set_cookie( app.config['AUTH_COOKIE_NAME'], '%s#%s' % (
        UserService.geneAuthCode(user_info), user_info.uid),  60 * 60 * 24 * 120)  # 保存120天
    return response

@route_user.route( "/edit",methods = [ "GET","POST" ] )
def edit():
    if request.method == "GET":

        #todo:my_render_template在通用的common.libs.Helper中
        # 就是获取g对象中的current_user添加进去，默认已经添加current_user了
        #current这个参数在模板渲染，用来进行高亮的显示，
        #edit.html页面中{% include "common/tab_user.html" %}引入tab_user，这样便于后期维护
        # 功能在templates/common/tab_user.html中
        return my_render_template( "user/edit.html",{ 'current':'edit' } )

    resp = { 'code':200,'msg':'操作成功~','data':{} }
    req = request.values
    nickname = req['nickname'] if 'nickname' in req else ''
    email = req['email'] if 'email' in req else ''

    if nickname is None or len( nickname ) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的姓名~~"
        return jsonify( resp )

    if email is None or len( email ) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的邮箱~~"
        return jsonify( resp )

    user_info = g.current_user
    user_info.nickname = nickname
    user_info.email = email

    db.session.add( user_info )
    db.session.commit()
    return jsonify(resp)

@route_user.route("/reset-pwd", methods=["GET", "POST"])
def resetPwd():
    if request.method == "GET":
        return my_render_template("user/reset_pwd.html", {'current': 'reset-pwd'})

    resp = {'code': 200, 'msg': '操作成功~', 'data': {}}
    req = request.values

    old_password = req['old_password'] if 'old_password' in req else ''
    new_password = req['new_password'] if 'new_password' in req else ''

    if old_password is None or len(old_password) < 6:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的原密码~~"
        return jsonify(resp)

    if new_password is None or len(new_password) < 6:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的新密码~~"
        return jsonify(resp)

    if old_password == new_password:
        resp['code'] = -1
        resp['msg'] = "请重新输入一个吧，新密码和原密码不能相同哦~~"
        return jsonify(resp)

    user_info = g.current_user

    if user_info.login_pwd != UserService.genePwd(old_password, user_info.login_salt):
        resp['code'] = -1
        resp['msg'] = "原密码不对~~"
        return jsonify(resp)

    if user_info.uid == 1:
        resp['code'] = -1
        resp['msg'] = "该用户是演示账号，不准修改密码和登录用户名~~"
        return jsonify(resp)

    user_info.login_pwd = UserService.genePwd(new_password, user_info.login_salt)

    db.session.add(user_info)
    db.session.commit()

    ###############################修改密码后需要重新生成cookie，否则拦截器的授权码还是以前
    # 的密码生成，会让重新登录
    response = make_response(json.dumps(resp))
    # 设置cookie，cookie名字在config.py中设置的名字AUTH_COOKIE_NAME：mooc_food
    # 通过#号拼接
    response.set_cookie(app.config['AUTH_COOKIE_NAME'], '%s#%s' % (
        UserService.geneAuthCode(user_info), user_info.uid), 60 * 60 * 24 * 120)  # 保存120天
    ################################
    return response


@route_user.route("/logout")
def logout():  # 清理cookie，跳到登录页面
    response = make_response(redirect(UrlManager.buildUrl("/user/login")))
    response.delete_cookie(app.config['AUTH_COOKIE_NAME'])
    return response