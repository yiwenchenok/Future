# -*- coding: utf-8 -*-
from flask import Blueprint, request, redirect, jsonify
from common.libs.Helper import my_render_template, iPagination, getCurrentDate
from web.models.member.Member import Member
from application import app, db
from common.libs.UrlManager import UrlManager
from web.models.member.MemberComments import MemberComments
from common.libs.Helper import *
from web.models.food.Food import Food
from web.models.payorder.PayOrder import PayOrder

route_member = Blueprint('member_page', __name__)


@route_member.route("/index")
def index():
    resp_data = {}
    req = request.values
    page = int(req['p']) if ('p' in req and req['p']) else 1  # 分页，前端逻辑写common\pagenation.html
    query = Member.query  # 获取数据库中的会员列表
    if 'mix_kw' in req:  # 搜索功能，通过ilike忽略大小写
        query = query.filter(Member.nickname.ilike("%{0}%".format(req['mix_kw'])))
    if 'status' in req and int(req['status']) > -1:  # 获取状态值，如果大于-1就可以进行搜索 （正常与删除两种状态）
        query = query.filter(Member.status == int(req['status']))  # 如果有状态的筛选，就只返回符合状态的会员列表
    ##分页对象要设置的参数
    page_params = {
        'total': query.count(),
        'page_size': app.config['PAGE_SIZE'],
        'page': page,
        'display': app.config['PAGE_DISPLAY'],
        'url': request.full_path.replace("&p={}".format(page), "")
    }
    pages = iPagination(page_params)  # #分页对象数据
    offset = (page - 1) * app.config['PAGE_SIZE']  # 偏移量 page为当前页数乘以偏移量
    # flask可以在查询的时候加入偏移量的操作
    list = query.order_by(Member.id.asc()).offset(offset).limit(app.config['PAGE_SIZE']).all()

    resp_data['list'] = list  # 将循环的会员数据，只返回当前页的会员列表
    resp_data['pages'] = pages  # 分页对象数据
    resp_data['search_con'] = req  # 所有的查询字段都放在req=request.values
    # 获取所有状态描述
    ''' STATUS_MAPPING = {"1":"正常","0":"已删除"} '''
    resp_data['status_mapping'] = app.config['STATUS_MAPPING']
    resp_data['current'] = 'index'
    return my_render_template("member/index.html", resp_data)


@route_member.route("/info")
def info():
    resp_data = {}
    req = request.args
    id = int(req.get("id", 0))
    reback_url = UrlManager.buildUrl("/member/index")
    if id < 1:
        return redirect(reback_url)
    info = Member.query.filter_by(id=id).first()
    if not info:
        return redirect(reback_url)
    pay_order_list = PayOrder.query.filter_by(member_id=id).filter(PayOrder.status.in_([-8, 1])) \
        .order_by(PayOrder.id.desc()).all()
    comment_list = MemberComments.query.filter_by(member_id=id).order_by(MemberComments.id.desc()).all()
    resp_data['comment_list'] = comment_list
    resp_data['pay_order_list'] = pay_order_list
    resp_data['info'] = info
    resp_data['current'] = 'index'
    return my_render_template("member/info.html", resp_data)


@route_member.route("/set", methods=["GET", "POST"])
def set():  # 修改会员名
    if request.method == "GET":
        resp_data = {}
        req = request.args
        id = int(req.get("id", 0))
        reback_url = UrlManager.buildUrl("/member/index")  # 重定向回主页面
        if id < 1:
            return redirect(reback_url)
        info = Member.query.filter_by(id=id).first()
        if not info:
            return redirect(reback_url)
        if info.status != 1:
            return redirect(reback_url)
        resp_data['info'] = info
        resp_data['current'] = 'index'
        return my_render_template("member/set.html", resp_data)
    resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}
    req = request.values
    id = req['id'] if 'id' in req else 0
    nickname = req['nickname'] if 'nickname' in req else ''
    if nickname is None or len(nickname) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的姓名~~"
        return jsonify(resp)
    member_info = Member.query.filter_by(id=id).first()
    if not member_info:
        resp['code'] = -1
        resp['msg'] = "指定会员不存在~~"
        return jsonify(resp)
    member_info.nickname = nickname
    member_info.updated_time = getCurrentDate()
    db.session.add(member_info)
    db.session.commit()
    return jsonify(resp)


@route_member.route("/ops", methods=["POST"])
def ops():  # 删除会员操作或恢复会员操作
    resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}
    req = request.values
    id = req['id'] if 'id' in req else 0
    act = req['act'] if 'act' in req else ''
    if not id:
        resp['code'] = -1
        resp['msg'] = "请选择要操作的账号~~"
        return jsonify(resp)
    if act not in ['remove', 'recover']:
        resp['code'] = -1
        resp['msg'] = "操作有误，请重试~~"
        return jsonify(resp)
    member_info = Member.query.filter_by(id=id).first()
    if not member_info:
        resp['code'] = -1
        resp['msg'] = "指定会员不存在~~"
        return jsonify(resp)
    if act == "remove":
        member_info.status = 0
    elif act == "recover":
        member_info.status = 1
    member_info.updated_time = getCurrentDate()  # 最新时间
    db.session.add(member_info)
    db.session.commit()
    return jsonify(resp)


@route_member.route("/comment")
def comment():  # 会员评论
    resp_data = {}
    req = request.args
    page = int(req['p']) if ('p' in req and req['p']) else 1
    query = MemberComments.query
    page_params = {
        'total': query.count(),
        'page_size': app.config['PAGE_SIZE'],
        'page': page,
        'display': app.config['PAGE_DISPLAY'],
        'url': request.full_path.replace("&p={}".format(page), "")
    }
    pages = iPagination(page_params)
    offset = (page - 1) * app.config['PAGE_SIZE']
    comment_list = query.order_by(MemberComments.id.desc()).offset(offset).limit(
        app.config['PAGE_SIZE']).all()  # 获取评论信息
    data_list = []
    if comment_list:
        member_map = getDictFilterField(Member, Member.id, "id", selectFilterObj(comment_list, "member_id"))#selectFilterObj返回member_id的值的列表
        food_ids = []
        for item in comment_list:
            tmp_food_ids = (item.food_ids[1:-1]).split("_")  # 获取评论表中的商品id，多个，以_分开，food_ids：储存格式为'_1_2'
            # tmp_food_ids数据为：['1', '2']
            food_ids = tmp_food_ids  # 赋值给全局变量food_ids，传递给Food模型取出菜品名单
        food_map = getDictFilterField(Food, Food.id, "id", food_ids)  # 从商品表中抽取评论表food_ids字段中的id值对应的商品信息，为后续取出商品名
        # print(food_map)
        '''
        Food:商品表的索引对象
        Food.id：商品表的id索引对象
        food_ids:['1', '2']
        "id":在商品表搜索的关键字
        '''
        for item in comment_list:
            tmp_member_info = member_map[item.member_id]
            # tmp_member_info的数据为：<Member 1><Member 2>...，为Member会员表的索引对象
            tmp_foods = []
            tmp_food_ids = (item.food_ids[1:-1]).split("_")
            # tmp_food_ids数据为：['1', '2']
            for tmp_food_id in tmp_food_ids:
                # tmp_food_id输出为：1 2  ...
                tmp_food_info = food_map[int(tmp_food_id)]
                # tmp_food_info输出为:<Food 1><Food 2>...Food模型商品表的各行的对象索引
                tmp_foods.append({
                    'name': tmp_food_info.name,  # 利用Food模型商品表的各行的对象索引获取对于的商品名称
                })
                # tmp_foods数据为       [{'name': '白切鸡'}]
                # 循环两次              [{'name': '白切鸡'}, {'name': '番茄炒鸡蛋'}]
            tmp_data = {
                "content": item.content,
                "score": item.score_desc,
                "member_info": tmp_member_info,
                "foods": tmp_foods
            }
            data_list.append(tmp_data)
    # print(data_list)
    # [{'content': '好吃', 'score': 8, 'member_info': < Member 1 >,
    # 'foods': [{'name': '白切鸡'}, {'name': '番茄炒鸡蛋'}]}]
    resp_data['list'] = data_list
    resp_data['pages'] = pages
    resp_data['current'] = 'comment'
    return my_render_template("member/comment.html", resp_data)
