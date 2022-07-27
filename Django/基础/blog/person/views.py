from django.shortcuts import render
from .models import User
from django.http import HttpResponse
from django.db.models import Q,F
# Create your views here.

"""
返回列表的过滤器如下：
all()：返回所有数据
filter()：返回满足条件的数据
exclude()：返回满足条件之外的数据，相当于sql语句中where部分的not关键字
order_by()：排序，参数为字段名，-号表示降序
返回单个值的过滤器如下：
get()：返回单个满足条件的对象
如果未找到会引发"模型类.DoesNotExist"异常
如果多条被返回，会引发"模型类.MultipleObjectsReturned"异常
count()：返回当前查询的总条数 exists()：判断查询集中是否有数据，如
果有则返回True，没有则返回False

"""

def index(request):
    #ilike
    # user_list = User.yt_objects.filter(username__startswith='a') #获取所有a开头的
    # user_list = User.yt_objects.filter(username__endswith = 'a') #获取所有a结尾的
    # user_list = User.yt_objects.filter(username__contains = 'a') #获取包含a的
    # user_list = User.yt_objects.filter(username__icontains = 'a') #获取包含a/A的
    # user_list = User.yt_objects.filter(username__isnull = False)  #返回不为null的所有用户
    # user_list = User.yt_objects.filter(id__in = [5,8,9])  #返回id为5,8,9的对象

    #思考1：返回id为5,8,9中的对象，并且以a开头
    # user_list = User.yt_objects.filter(id__in=[5, 8, 9]).filter(username__startswith='a')
    #上面方法的简写:同时满足多个条件
    # user_list = User.yt_objects.filter( Q(id__in=[5, 8, 9]) & Q(username__startswith='a')) #&表示与
    #Q对象的逻辑与可以简写如下
    # user_list = User.yt_objects.filter(id__in=[5, 8, 9],username__startswith='a')

    # 思考2：返回id为5,8,9中的对象 或者 以a开头
    #Q对象的逻辑或则无法简写
    # user_list = User.yt_objects.filter(Q(id__in=[5, 8, 9]) | Q(username__startswith='a')) #|表示或

    #思考3：返回modify_time大于create_time
    user_list = User.yt_objects.filter(modify_time__gt=F('create_time')) #F('create_time')表示的本身的create_time字段


    # user_list = User.yt_objects.filter(id__gt = 5) #获取所有id大于5的用户
    # user_list = User.yt_objects.filter(id__lte = 6) #获取所有id小于等于6的用户
    # user_list = User.yt_objects.filter(id = 6) #获取id等于6的用户 todo:返回列表 get(id = 6) #获取id等于6的用户 todo:返回对象
    # user_list = User.yt_objects.filter(id__exact = 6) #效果等价于上一条
    # user_list = User.yt_objects.exclude(id__exact = 6) #取所有的id不等于6的用户
    str_ = ""
    for p in user_list:
        str_ += f"作者名{p.id}:" + p.username + "\t"

    return HttpResponse(str_)



def save_user(request,us):

    #方法1:
    # u = User()
    # u.username = us
    # u.desc = "很帅气。啦啦啦啦啦啦"
    # u.age = 12
    # u.height = 1.9
    # u.save() #保存

    #方法2：自定义create方法，在models里面
    u = User.yt_objects.create(us,"很帅气。啦啦啦啦啦啦",12,1.9)
    u.save()
    return HttpResponse("save_user ok~")

def delete_user(request,id):
    # u = User.objects.get(pk=id) #根据id获取实例对象
    u = User.yt_objects.get(pk=id) #根据id获取实例对象  #todo:3.将默认的objects改成自定义的管理器
    # u.delete() #删除数据，物理删除  todo：尽量不要使用物理删除

    #推荐逻辑删除
    u.is_delete = True
    u.save()

    return HttpResponse("delete_user ok~")