# -*- coding: utf-8 -*-
from flask import Blueprint, request, redirect, jsonify
from common.libs.Helper import my_render_template, iPagination, getCurrentDate
from common.libs.UrlManager import UrlManager
from common.libs.user.UserService import UserService  # 加解密机制
from web.models.User import User
from sqlalchemy import or_
from application import app, db

route_account = Blueprint('account_page', __name__)


@route_account.route("/index")
def index():
    resp_data = {}
    req = request.values
    page = int(req['p']) if ('p' in req and req['p']) else 1  # 初始化页码为1，有传递的参数req['p']，则使用其参数，服务于分页处理
    query = User.query
    # 搜索框功能
    if 'mix_kw' in req:  # mix_kw：搜索框传递回来的字符串，以手机号或者管理者呢称搜索。or_：两者有一即可
        rule = or_(User.nickname.ilike("%{0}%".format(req['mix_kw'])), User.mobile.ilike("%{0}%".format(req['mix_kw'])))
        query = query.filter(rule)
    if 'status' in req and int(req['status']) > -1:
        query = query.filter(User.status == int(req['status']))  # 获取状态对应的信息
    page_params = {
        'total': query.count(),  # 数据总数
        'page_size': app.config['PAGE_SIZE'],  # 分页的个数
        'page': page,  # 页码
        'display': app.config['PAGE_DISPLAY'],  # 演示多少页
        'url': request.full_path.replace("&p={}".format(page), "")
    }
    pages = iPagination(page_params)  # 分页，返回字典ret{}
    # 分页功能主要是传递回来的page页码数
    offset = (page - 1) * app.config['PAGE_SIZE']  # offset：输出的数据的第一个排序
    limit = app.config['PAGE_SIZE'] * page  # limit：输出的数据的最后一个排序
    list = query.order_by(User.uid.asc()).all()[offset:limit]  # 以分页的个数限制每页输出的个数，并且以管理员的uid进行降序排序
    resp_data['list'] = list  # 用于管理员的信息管理index.html
    resp_data['pages'] = pages  # 用于分页pagenation.html
    resp_data['search_con'] = req  # 前端传来的数据，传回去
    resp_data['status_mapping'] = app.config['STATUS_MAPPING']  # 传管理员状态说明到前端，作为渲染
    return my_render_template("account/index.html", resp_data)


@route_account.route("/info")
def info():
    resp_data = {}
    req = request.args  # args：获取请求链接？后面携带的参数
    uid = int(req.get('id', 0))  # 获取id的值，没有则0
    reback_url = UrlManager.buildUrl("/account/index")  # 构造返回函数
    if uid < 1:
        return redirect(reback_url)
    info = User.query.filter_by(uid=uid).first()
    if not info:
        return redirect(reback_url)
    resp_data['info'] = info
    return my_render_template("account/info.html", resp_data)


@route_account.route("/set", methods=["GET", "POST"])
def set():
    default_pwd = "******"
    if request.method == "GET":
        resp_data = {}
        req = request.args
        uid = int(req.get("id", 0))
        info = None
        if uid:
            info = User.query.filter_by(uid=uid).first()
        resp_data['info'] = info
        return my_render_template("account/set.html", resp_data)
    resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}
    req = request.values
    id = req['id'] if 'id' in req else 0
    nickname = req['nickname'] if 'nickname' in req else ''
    mobile = req['mobile'] if 'mobile' in req else ''
    email = req['email'] if 'email' in req else ''
    login_name = req['login_name'] if 'login_name' in req else ''
    login_pwd = req['login_pwd'] if 'login_pwd' in req else ''
    if nickname is None or len(nickname) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的姓名~~"
        return jsonify(resp)
    if mobile is None or len(mobile) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的手机号码~~"
        return jsonify(resp)
    if email is None or len(email) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的邮箱~~"
        return jsonify(resp)
    if login_name is None or len(login_name) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的登录用户名~~"
        return jsonify(resp)
    if login_pwd is None or len(email) < 6:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的登录密码~~"
        return jsonify(resp)
    has_in = User.query.filter(User.login_name == login_name, User.uid != id).first()
    if has_in:
        resp['code'] = -1
        resp['msg'] = "该登录名已存在，请换一个试试~~"
        return jsonify(resp)
    user_info = User.query.filter_by(uid=id).first()
    # 判断是修改还是添加账号
    if user_info:
        model_user = user_info
    else:
        model_user = User()
        model_user.created_time = getCurrentDate()
        model_user.login_salt = UserService.geneSalt()
    model_user.nickname = nickname
    model_user.mobile = mobile
    model_user.email = email
    model_user.login_name = login_name
    # 判断是否已经修改密码
    if login_pwd != default_pwd:  # default_pwd：'******'
        if user_info and user_info.uid == 1:
            resp['code'] = -1
            resp['msg'] = "该用户是演示账号，不准修改密码和登录用户名~~"
            return jsonify(resp)
        model_user.login_pwd = UserService.genePwd(login_pwd, model_user.login_salt)
    model_user.updated_time = getCurrentDate()
    db.session.add(model_user)
    db.session.commit()
    return jsonify(resp)


@route_account.route("/ops", methods=["POST"])
def ops():  # 管理员状态的修改，1：正常，0：删除
    resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}
    req = request.values
    id = req['id'] if 'id' in req else 0
    act = req['act'] if 'act' in req else ''  # 判断点击的是什么操作 remove 或 recover
    if not id:
        resp['code'] = -1
        resp['msg'] = "请选择要操作的账号~~"
        return jsonify(resp)

    if act not in ['remove', 'recover']:
        resp['code'] = -1
        resp['msg'] = "操作有误，请重试~~"
        return jsonify(resp)
    user_info = User.query.filter_by(uid=id).first()
    if not user_info:
        resp['code'] = -1
        resp['msg'] = "指定账号不存在~~"
        return jsonify(resp)
    if act == "remove":  # 删除管理员，状态修改为0
        user_info.status = 0
    elif act == "recover":  # 恢复管理员，状态修改为1
        user_info.status = 1
    if user_info and user_info.uid == 1:
        resp['code'] = -1
        resp['msg'] = "该用户是演示账号，不准操作账号~~"
        return jsonify(resp)
    user_info.update_time = getCurrentDate()
    db.session.add(user_info)
    db.session.commit()
    return jsonify(resp)
