# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify, redirect
from common.libs.Helper import my_render_template, getCurrentDate, iPagination, getDictFilterField
from application import app, db
from web.models.food.Food import Food
from web.models.food.FoodCat import FoodCat
from web.models.food.FoodStockChangeLog import FoodStockChangeLog
from common.libs.UrlManager import UrlManager
from common.libs.food.FoodService import FoodService
from decimal import Decimal
from sqlalchemy import or_

route_food = Blueprint('food_page', __name__)

"""
后台美食管理

"""


@route_food.route("/index")
def index():
    resp_data = {}
    req = request.values
    page = int(req['p']) if ('p' in req and req['p']) else 1
    query = Food.query
    if 'mix_kw' in req:
        rule = or_(Food.name.ilike("%{0}%".format(req['mix_kw'])),
                   Food.tags.ilike("%{0}%".format(req['mix_kw'])))
        query = query.filter(rule)
    if 'status' in req and int(req['status']) > -1:
        query = query.filter(Food.status == int(req['status']))
    if 'cat_id' in req and int(req['cat_id']) > 0:
        query = query.filter(Food.cat_id == int(req['cat_id']))
    page_params = {
        'total': query.count(),
        'page_size': app.config['PAGE_SIZE'],
        'page': page,
        'display': app.config['PAGE_DISPLAY'],
        'url': request.full_path.replace("&p={}".format(page), "")
    }

    pages = iPagination(page_params)
    offset = (page - 1) * app.config['PAGE_SIZE']
    list = query.order_by(Food.id.desc()).offset(offset).limit(app.config['PAGE_SIZE']).all()
    '''
    cat_mapping:跨表查询并输出前端 
    getDictFilterField()根据某个字段获取一个dic出来
    '''
    cat_mapping = getDictFilterField(FoodCat, None, "id", None)
    #print(cat_mapping)：{1: <FoodCat 1>, 2: <FoodCat 2>}
    resp_data['list'] = list
    resp_data['pages'] = pages
    resp_data['search_con'] = req
    resp_data['status_mapping'] = app.config['STATUS_MAPPING']
    resp_data['cat_mapping'] = cat_mapping
    resp_data['current'] = 'index'
    return my_render_template("food/index.html", resp_data)


@route_food.route("/info")
def info():  # 菜品的详细信息
    resp_data = {}
    req = request.args  # request.args：获取请求链接中？后面的全部参数
    id = int(req.get("id", 0))  # 获取id的参数，没有则为0
    reback_url = UrlManager.buildUrl("/food/index")  # 构建判断请求的id不存在，返回主页
    if id < 1:  # 菜单是以1为单位开始排序
        return redirect(reback_url)
    info = Food.query.filter_by(id=id).first()
    if not info:
        return redirect(reback_url)
    stock_change_list = FoodStockChangeLog.query.filter(FoodStockChangeLog.food_id == id) \
        .order_by(FoodStockChangeLog.id.desc()).all()  # 获取该菜品的库存变化信息并以id为降序排序
    resp_data['info'] = info  # info为Foodmodel的实例
    resp_data['stock_change_list'] = stock_change_list  # stock_change_list为菜品的库存变化信息
    resp_data['current'] = 'index'
    return my_render_template("food/info.html", resp_data)


@route_food.route("/set", methods=['GET', 'POST'])
def set():
    if request.method == "GET":
        resp_data = {}
        req = request.args
        id = int(req.get('id', 0))
        info = Food.query.filter_by(id=id).first()
        if info and info.status != 1:
            return redirect(UrlManager.buildUrl("/food/index"))
        cat_list = FoodCat.query.all()
        resp_data['info'] = info
        resp_data['cat_list'] = cat_list
        resp_data['current'] = 'index'
        return my_render_template("food/set.html", resp_data)
    resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}
    req = request.values
    id = int(req['id']) if 'id' in req and req['id'] else 0
    cat_id = int(req['cat_id']) if 'cat_id' in req else 0
    name = req['name'] if 'name' in req else ''
    price = req['price'] if 'price' in req else ''
    main_image = req['main_image'] if 'main_image' in req else ''
    summary = req['summary'] if 'summary' in req else ''
    stock = int(req['stock']) if 'stock' in req else ''
    tags = req['tags'] if 'tags' in req else ''
    if cat_id < 1:
        resp['code'] = -1
        resp['msg'] = "请选择分类~~"
        return jsonify(resp)
    if name is None or len(name) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的名称~~"
        return jsonify(resp)
    if not price or len(price) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的售卖价格~~"
        return jsonify(resp)
    price = Decimal(price).quantize(Decimal('0.00'))  # 将价格精确到小数后两位
    if price <= 0:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的售卖价格~~"
        return jsonify(resp)
    if main_image is None or len(main_image) < 3:
        resp['code'] = -1
        resp['msg'] = "请上传封面图~~"
        return jsonify(resp)
    if summary is None or len(summary) < 3:
        resp['code'] = -1
        resp['msg'] = "请输入图书描述，并不能少于10个字符~~"
        return jsonify(resp)
    if stock < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的库存量~~"
        return jsonify(resp)
    if tags is None or len(tags) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入标签，便于搜索~~"
        return jsonify(resp)
    food_info = Food.query.filter_by(id=id).first()
    before_stock = 0  # 初始化库存
    if food_info:  # 判断：如果该菜品存在，就是在修改菜品的页面
        model_food = food_info  # 获取该菜品的信息
        before_stock = model_food.stock  # 获取该菜品的库存
    else:
        model_food = Food()  # 判断：如果该菜品不存在，就是在创建菜品的页面
        model_food.status = 1  # 设置新创建菜品状态为1
        model_food.created_time = getCurrentDate()  # 创建时间
    model_food.cat_id = cat_id
    model_food.name = name
    model_food.price = price
    model_food.main_image = main_image
    model_food.summary = summary  # 菜品概述
    model_food.stock = stock
    model_food.tags = tags
    model_food.updated_time = getCurrentDate()
    db.session.add(model_food)
    db.session.commit()
    FoodService.setStockChangeLog(model_food.id, int(stock) - int(before_stock), "后台修改")  # 修改库存信息
    return jsonify(resp)


@route_food.route("/cat")
def cat():
    resp_data = {}
    req = request.values
    query = FoodCat.query
    if 'status' in req and int(req['status']) > -1:
        query = query.filter(FoodCat.status == int(req['status']))
    list = query.order_by(FoodCat.weight.desc(), FoodCat.id.desc()).all()
    resp_data['list'] = list
    resp_data['search_con'] = req
    resp_data['status_mapping'] = app.config['STATUS_MAPPING']
    resp_data['current'] = 'cat'
    return my_render_template("food/cat.html", resp_data)


@route_food.route("/cat-set", methods=["GET", "POST"])  # get数据展示，post做数据提交
def catSet():
    """编辑和删除页面：cat-set.html"""
    if request.method == "GET":
        resp_data = {}
        req = request.args
        id = int(req.get("id", 0))
        info = None
        if id:  # 是否传id值来区分是  编辑的请求 / 展示请求
            info = FoodCat.query.filter_by(id=id).first()
        resp_data['info'] = info
        resp_data['current'] = 'cat'
        return my_render_template("food/cat_set.html", resp_data)

    resp = {'code': 200, 'msg': '操作成功~~', 'data': {}}
    req = request.values

    id = req['id'] if 'id' in req else 0
    name = req['name'] if 'name' in req else ''
    weight = int(req['weight']) if ('weight' in req and int(req['weight']) > 0) else 1

    if name is None or len(name) < 1:
        resp['code'] = -1
        resp['msg'] = "请输入符合规范的分类名称~~"
        return jsonify(resp)

    food_cat_info = FoodCat.query.filter_by(id=id).first()
    if food_cat_info:
        model_food_cat = food_cat_info
    else:
        model_food_cat = FoodCat()
        model_food_cat.created_time = getCurrentDate()
    model_food_cat.name = name
    model_food_cat.weight = weight
    model_food_cat.updated_time = getCurrentDate()
    db.session.add(model_food_cat)
    db.session.commit()
    return jsonify(resp)


@route_food.route("/cat-ops", methods=["POST"])
def catOps():
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

    food_cat_info = FoodCat.query.filter_by(id=id).first()
    if not food_cat_info:
        resp['code'] = -1
        resp['msg'] = "指定分类不存在~~"
        return jsonify(resp)

    if act == "remove":
        food_cat_info.status = 0
    elif act == "recover":
        food_cat_info.status = 1

        food_cat_info.update_time = getCurrentDate()
    db.session.add(food_cat_info)
    db.session.commit()
    return jsonify(resp)


@route_food.route("/ops", methods=["POST"])
def ops():
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

    food_info = Food.query.filter_by(id=id).first()
    if not food_info:
        resp['code'] = -1
        resp['msg'] = "指定美食不存在~~"
        return jsonify(resp)

    if act == "remove":
        food_info.status = 0
    elif act == "recover":
        food_info.status = 1

    food_info.updated_time = getCurrentDate()
    db.session.add(food_info)
    db.session.commit()
    return jsonify(resp)
