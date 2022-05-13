import json

from django.db.models import Q, Sum
from django.http import JsonResponse
from django.shortcuts import render
from .models import JDProductData,user
from django.core.cache import cache
from django.shortcuts import redirect
from django.urls import reverse
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    """
    首页
    :param request:
    :return:
    """
    key_word = request.GET.get('key_word', '')
    products = JDProductData.objects.all().order_by('id')
    if key_word:
        products = products.filter(Q(p_name__contains=key_word) | Q(p_shop__contains=key_word))
    return render(request, 'home.html', context={'products': products, 'key_word': key_word})
def product_detail(request):
    """
    商品详情
    :param request:
    :return:
    """
    p_id = request.GET.get('p_id')
    JD_data = JDProductData.objects.get(id=p_id)
    JD_data.p_detail = json.loads(JD_data.p_detail)
    return render(request, 'detail.html', {'JD_data': JD_data})
def product_analyze(request):
    """
    分析界面
    :param request:
    :return:
    """
    return render(request, 'jd_echarts.html')


def product_data(request):
    """
    数据分析用的到的数据
    :param request:
    :return:
    """
    # 价格和销量结果统计
    sale_price = JDProductData.objects.values_list('p_price').annotate(Sum('p_sale'))
    price_list, price_sale_list = zip(*list(sale_price))

    # 统计不同性别销量
    gender_sale = JDProductData.objects.values_list('p_gender').annotate(Sum('p_sale'))
    gender_list, gender_sale_list = zip(*list(gender_sale))

    # 性别统计饼图
    gen_sale_pie = []
    for item in gender_sale:
        gen_sale_pie.append({
            'name': item[0],
            'value': item[1]
        })
    # 获取销量top10店铺
    top10_shop_obj = JDProductData.objects.values_list('p_shop').annotate(Sum('p_sale'))
    top_shop_list, top_shop_sale = zip(*sorted(top10_shop_obj, key=lambda vale: vale[1], reverse=True)[:10])

    # 获取销量top10 品牌
    top10_pinpai_obj = JDProductData.objects.values_list('p_pinpai').annotate(Sum('p_sale'))
    top_pinpai_list, top_pinpai_sale = zip(*sorted(top10_pinpai_obj, key=lambda vale: vale[1], reverse=True)[:10])
    data = cache.get('data', '')
    if data:
        res = data
    else:
        data = {
            'price_sale': [price_list, price_sale_list],
            'gender_sale_line': [gender_list, gender_sale_list],
            'gen_sale_pie': gen_sale_pie,
            'top10_shop_line': [top_shop_list, top_shop_sale],
            'top10_pinpai_line': [top_pinpai_list, top_pinpai_sale]
        }
        cache.set('data', data, 60*60*12)
        res = data

    return JsonResponse(res)

def login(request):
    return render(request,'login.html')


def logout(request):
    del request.session['user']
    return redirect(reverse('login'))


def dologin(request):
    '''执行登录'''
    try:
        #根据登录账号获取用户信息
        User = user.objects.get(name=request.POST['name'])
        s = request.POST['password']
        # 校验密码是否正确
        if User.password == s:
            request.session['user'] = User.toDict()
            return redirect(reverse('home'))
        else:
            context = {"info": "登录密码错误！"}
            return render(request, "login.html", context)
    except Exception as err:
        print(err)
        context={"info":"登录账号不存在！"}
    return render(request, "login.html", context)


def register(request):
    return render(request,'register.html')
def register_doing(request):
    try:
        option = user()
        option.name = request.POST['name']
        option.password = request.POST['password']
        option.save()
    except Exception as err:
        print(err)
        return redirect(reverse('register'))
    return redirect(reverse('login'))


def product_manage(request,pIndex=1):
    # 执行分页处理
    option = JDProductData.objects.all()
    pIndex = int(pIndex)
    page = Paginator(option, 5)  # 以5条每页创建分页对象
    maxpages = page.num_pages  # 最大页数
    # 判断页数是否越界
    if pIndex > maxpages:
        pIndex = maxpages
    if pIndex < 1:
        pIndex = 1
    list2 = page.page(pIndex)  # 当前页数据
    plist = page.page_range  # 页码数列表
    # 封装信息加载模板输出
    context = {"userlist": list2, 'plist': plist, 'pIndex': pIndex, 'maxpages': maxpages, }
    return render(request,'manage.html',context)
def delete(request,uid):
    try:
        ob = JDProductData.objects.get(id=uid)
        ob.delete()
        context={"info":"删除成功！"}
    except Exception as err:
        print(err)
        context={"info":"删除失败"}
    return JsonResponse(context)
def edit(request,uid):
    option = JDProductData.objects.get(id=uid)
    context = {"option": option}
    return render(request, "edit.html", context)

'''执行编辑信息'''

def update(request,uid):
    try:
        ob = JDProductData.objects.get(id=uid)
        ob.p_name = request.POST['p_name']
        ob.p_price = request.POST['p_price']
        ob.p_imag_scr = request.POST['p_imag_scr']
        ob.p_shop = request.POST['p_shop']
        ob.p_comment_count = request.POST['p_comment_count']
        ob.p_sale = request.POST['p_sale']
        ob.p_pinpai = request.POST['p_pinpai']
        ob.p_gender = request.POST['p_gender']
        ob.save()
        context={"info":"修改成功！"}
    except Exception as err:
        print(err)
        context={"info":"修改失败"}
    # return JsonResponse(context)
    return render(request,"info.html",context)


'''加载添加页面'''
def add(request):
    return render(request,"add.html")
'''执行添加'''
def insert(request):
    try:
        ob = JDProductData()
        ob.product_id = request.POST['product_id']
        ob.p_name = request.POST['p_name']
        ob.p_price = request.POST['p_price']
        ob.p_imag_scr = request.POST['p_imag_scr']
        ob.p_shop = request.POST['p_shop']
        ob.p_comment_count = request.POST['p_comment_count']
        ob.p_sale = request.POST['p_sale']
        ob.p_pinpai = request.POST['p_pinpai']
        ob.p_gender = request.POST['p_gender']
        ob.p_detail = request.POST['p_detail']
        ob.save()
        context={"info":"添加成功！"}
    except Exception as err:
        print(err)
        context={"info":"添加失败"}
    return render(request,"info.html",context)