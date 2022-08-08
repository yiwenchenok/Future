# -*- coding: utf-8 -*-
from flask import g, render_template
import datetime

'''
自定义分页类
'''
def iPagination(params):
    import math
    ret = {
        "is_prev": 1,  # 是否有上一页
        "is_next": 1,
        "from": 0,
        "end": 0,
        "current": 0,
        "total_pages": 0,
        "page_size": 0,
        "total": 0,
        "url": params['url'].replace("&p=", "")
    }
    total = int(params['total'])
    page_size = int(params['page_size'])
    page = int(params['page'])
    display = int(params['display'])
    total_pages = int(math.ceil(total / page_size))
    total_pages = total_pages if total_pages > 0 else 1
    if page <= 1:
        ret['is_prev'] = 0
    if page >= total_pages:
        ret['is_next'] = 0
    semi = int(math.ceil(display / 2))
    if page - semi > 0:
        ret['from'] = page - semi
    else:
        ret['from'] = 1
    if page + semi <= total_pages:
        ret['end'] = page + semi
    else:
        ret['end'] = total_pages
    ret['current'] = page
    ret['total_pages'] = total_pages
    ret['page_size'] = page_size
    ret['total'] = total
    ret['range'] = range(ret['from'], ret['end'] + 1)
    '''{'is_prev': 0, 'is_next': 0, 'from': 1, 'end': 1, 'current': 1, 
    'total_pages': 1, 'page_size': 50, 'total': 2, 'url': '/food/index?', 
    'range': range(1, 2)}'''
    print(ret)
    return ret



'''
统一渲染方法 改写rend_template
修改密码时，通过g获取到登录状态，变量名为current_user，
如果获取则为登录状态
'''
def my_render_template(template, context={}):
    if 'current_user' in g:
        context['current_user'] = g.current_user
    return render_template(template, **context)


'''
获取当前时间
'''
def getCurrentDate(format="%Y-%m-%d %H:%M:%S"):
    # return datetime.datetime.now().strftime( format )
    return datetime.datetime.now()


'''
获取格式化的时间
'''
def getFormatDate(date=None, format="%Y-%m-%d %H:%M:%S"):
    if date is None:
        date = datetime.datetime.now()
    return date.strftime(format)


'''
根据某个字段获取一个dic出来：两种方法 db_model+key_field
db_model：需要数据的数据库
key_field：需要从数据库判断的字段
select_filed：判断条件 例如以商品表中的商品分类id作为依据抽取对于分类名 FoodCat.id
id_list：判断条件的结合  
两种方法 
一、db_model+key_field
二、db_model+select_filed+id_list
'''

#跨表查询，遍历输出
def getDictFilterField(db_model, select_filed,key_field,id_list):  # FoodCat,FoodCat.id,"id",[]
    '''
    db_model：             Food:商品表的索引对象
    select_filed：        Food.id：商品表的id索引对象
    key_field：          "id":在商品表搜索的关键字
    id_list：            food_ids:['1', '2']
    '''
    ret = {}
    query = db_model.query
    if id_list and len(id_list) > 0:
        query = query.filter(select_filed.in_(id_list))
    #  print(query)   query返回的是sql语句，数据如下
    # SELECT `member`.id AS member_id, `member`.nickname AS member_nickname,
        # `member`.mobile AS member_mobile, `member`.sex AS member_sex, `member`.avatar AS member_avatar,
        # `member`.salt AS member_salt, `member`.reg_ip AS member_reg_ip, `member`.status AS member_status,
        # `member`.updated_time AS member_updated_time, `member`.created_time AS member_created_time
    # FROM `member`
    # WHERE `member`.id IN (__[POSTCOMPILE_id_1])
    list = query.all()
    #list：[<Member 1>, <Member 2>]
    if not list:
        return ret
    for item in list:
        if not hasattr(item, key_field):#hasattr() 函数用于判断对象是否包含对应的属性
            break #如果不存在key_field,退出循环
        ret[getattr(item, key_field)] = item
        #getattr：获取对象的值，函数中获取item里面的‘id’关键字的值
    # print(ret) ：{1: <Food 1>, 2: <Food 2>}
    return ret


# 通过field的值查找对应的model返回需要的数值列表
def selectFilterObj(obj, field): #comment_list, "member_id"
    ret = []
    for item in obj:
        #print(item): <MemberComments 1> <MemberComments 2>
        if not hasattr(item, field):
            break
        if getattr(item, field) in ret:
            continue
        ret.append(getattr(item, field))
    #print(ret):  [2, 1]
    return ret

def getDictListFilterField( db_model,select_filed,key_field,id_list ):
    ret = {}
    query = db_model.query
    if id_list and len( id_list ) > 0:
        query = query.filter( select_filed.in_( id_list ) )

    list = query.all()
    if not list:
        return ret
    for item in list:
        if not hasattr( item,key_field ):
            break
        if getattr( item,key_field ) not in ret:
            ret[getattr(item, key_field)] = []

        ret[ getattr( item,key_field ) ].append(item )
    return ret
