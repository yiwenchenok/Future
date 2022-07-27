import hashlib
import uuid

from django.shortcuts import render,get_object_or_404
#HttpResponseRedirect 重定向返回
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from .models import Post,Tag#导入模型类 文章
from person.models import User
from django.http import HttpResponseRedirect
#发送邮件
from django.core.mail import send_mail,send_mass_mail
from blog.settings import EMAIL_FROM

"""
模板渲染：
1.加载模板：loader.get_template
2.添加上下文：RequestContext
3.渲染模板： template.render
"""
#发送邮件
def send_m(request):
    html_message = "<a href='https://www.baidu.com'>欢迎来到羊驼老师的课堂</a>"
    try:
        send_mail('羊驼老师的课堂','欢迎~',EMAIL_FROM,recipient_list=["1820312463@qq.com"],html_message=html_message)
        return HttpResponse("send_mail发送成功")
    except Exception as e:
        return HttpResponse("send_mail发送失败",e)
#批量发送邮件
def send_m_2(request):
    html_message = "<a href='https://www.baidu.com'>欢迎来到羊驼老师的课堂</a>"
    msg1 = ('羊驼老师的课堂',html_message,EMAIL_FROM,["1820312463@qq.com"])
    msg2 = ('羊驼老师的课堂',html_message,EMAIL_FROM,["978506662@qq.com"])
    try:
        send_mass_mail((msg1,msg2))
        return HttpResponse("send_mass_mail发送成功")
    except Exception as e:
        return HttpResponse("send_mass_mail发送失败",e)
#上传图片
def pic_load(request):
    if request.method == "GET":
        return render(request,'myblog/pic_upload.html')
    elif request.method == "POST":
        #django提供保存图片的类
        from django.core.files.storage import FileSystemStorage
        # img = request.POST.get("pic")  #获取post请求中的参数
        img = request.FILES.get("pic")  #获取上传的文件
        name = str(uuid.uuid4()).replace("-", "") + ".png"  # 时间撮，命名空间，随机数，伪随机数保证id唯一性
        f = FileSystemStorage()
        # img_path = f.save(f"myblog/{img.name}",img)  #将img存储到 /static/media/myblog/xxx.png
        img_path = f.save(f"myblog/{name}",img)  #将img存储到 /static/media/myblog/xxx.png
        p = Post.objects.get(id=6)  #假定id为6的文章使我们需要修改封面的对象
        print(p.title)
        p.image = img_path  #myblog/xxx.png
        p.save()
        return HttpResponse("ok")
#过滤器-转义
def zy(request):
    html = "<h1> hello world</h1>"
    html2 = "<p> hello world</p>"
    return render(request,'myblog/zy.html',context={'html':html,'html2':html2})

'''def index(request):
#todo:orm操作
    plist = Post.objects.all()  #获取所有的文章实例
    # plist = Post.objects.filter(title__contains='我')  #获取所有的文章标题中包含 我的 文章
    # plist = Post.objects.filter(category_id=1)  #获取分类为mysql的文章 ,不推荐
    # plist = Post.objects.filter(category__category_name='msyql')  #获取分类为mysql的文章 ,推荐
    # plist = Post.objects.filter(category__category_name__in=["django",'msyql'])  #获取分类为django的文章 ,推荐
    #todo:返回所有分类为mysql的文章
    #方法1：通过文章类 去获取相应分类的所有文章  todo:关联查询 父类__父类字段
    # plist = Post.objects.filter(category__category_name='msyql')
    #方法2：通过 分类 去 获取 相应分类的所有文章  todo:反向查询  xxx.post_set.all()
    # cat = Category.objects.get(category_name='msyql')
    # plist = cat.post_set.all()  #查询到cat关联的所有的xxx,写法就是xxx_set
    #todo:聚合查询
    #查询创建时间最新的一篇文章
    # plist= Post.objects.all().order_by('-pub_time')[:1]
    # idmax = Post.objects.aggregate(Max('id'))  #返回对象  {'id__max': 5}
    # plist = Post.objects.filter(id= idmax['id__max'])[:1]
    # print(Post.objects.aggregate(Sum('id')))  #求和  {'id__sum': 15}
    return render(request,'index.html',context={"ps":plist})  #  返回给模板   '''
def index(request):
    page_num = request.GET.get("p",None)
    print(page_num)
    if not page_num:
        page_num = 1
    plist = Post.objects.all()  #获取所有的文章实例
    #todo:分页
    from django.core.paginator import Paginator
    pagn = Paginator(plist,4)  #将所有的文章实例进行分页，每一页2个数据
    #根据动态路由中page_num返回分页对象（可迭代对象）
    plist = pagn.page(page_num)  #page对象
    return render(request, 'myblog/index.html', context={"ps":plist})  #  返回给模板
def detail(request,id):
    # p = Post.objects.get(pk=id)  # 获取主键id为url所传的num的文章实例
    p = get_object_or_404(Post,pk=id) # 获取主键id为url所传的num的文章实例  推荐  没查询到就返回404
    return render(request, 'myblog/detail.html', context={'p':p, 'addr': "广州", "age":18})

#todo:类视图的写法
from django.views.generic import ListView
class Index(ListView):
    model = Post #模型类
    template_name = 'myblog/index.html'  #模板
    context_object_name = 'ps' #上下文
class Detail(Index):
    template_name = 'myblog/detail.html'  # 模板
    context_object_name = 'p'  # 上下文
    def get_queryset(self):
        """
        返回数据集
        :return:
        """
        #self.args获取在url中提取到的参数，所有的参数都会保存在self.args
        return self.model.objects.get(id=self.args[0])
    def get_context_data(self, **kwargs):
        """
        添加额外的上下文
        :param kwargs:
        :return:
        """
        #获取父类的上下文
        context = super(Detail,self).get_context_data()
        #添加额外的上下文
        context['addr'] = "广州"
        context["age"] = 18
        return context

#todo:session 的建立，展示，删除
#如何确 保数据的安全性呢，那就是将数据保存在服务端。这就利用到session技术。
def set_session(request):
    """设置session"""
    print(request.session) #<django.contrib.sessions.backends.db.SessionStore object at 0x000001E6B0838198>
    m = hashlib.md5()
    str = 'yangtuo'
    m.update(str.encode("utf-8"))
    request.session['name3']  = m.hexdigest()
    #2da474673e951b9e33aeb80290eb0501
    print(m.hexdigest()) #2da474673e951b9e33aeb80290eb0501
    request.session['name4']  = "jiuwei"
    request.session['name']  = "yangtuo"
    request.session['name2']  = "jiuwei"
    return HttpResponse("ok")
def get_session(request):
    """获取session"""
    name = request.session.get("name")
    name2 = request.session.get("name2")
    _auth_user_id = request.session.get("_auth_user_id")
    _auth_user_hash = request.session.get("_auth_user_hash")
    return JsonResponse({'name':name,'name2':name2,'_auth_user_id':_auth_user_id,'_auth_user_hash':_auth_user_hash})
def del_session(request):
    """删除session"""
    #1.删除单个
    # del request.session['name']
    # del request.session['name2']
    #2.清空数据，但是保留session_key
    # request.session.clear()
    #3.删除整个会话,不会保留key
    request.session.flush()
    return HttpResponse("删除session  ok")

#todo:cookie的建立，展示，删除
def set_cookie(request):
    """设置cookie"""
    resp = HttpResponse("设置cookie")
    resp.set_cookie( 'name', value='yangtuo')
    resp.set_cookie( 'name2', value='pydjango')
    return resp
def get_cookie(request):
    """获取cookie"""
    dic = {}
    dic["name"] = request.COOKIES.get('name')
    dic["name2"] = request.COOKIES.get('name2')
    return JsonResponse(dic)
def del_cookie(request):
    """删除cookie"""
    # request.COOKIES.clear() #清除本次会话的cookie
    print(request.COOKIES) #{}  {'name': 'yangtuo', 'name2': 'pydjango'}
    resp = HttpResponse("删除cookie")
    # resp.delete_cookie('name')
    # resp.delete_cookie('name2')
    return resp

#todo:响应-HttpResponse
def resp(request):
    """
    content：表示返回的内容
    charset：表示response采用的编码字符集，默认为utf-8
    status：返回的HTTP响应状态码
    content-type：指定返回数据的的MIME类型，默认为'text/html'
    :param request:
    :return:
    """
    resp = HttpResponse(content='ok',status=888)
    return resp

#进行登录界面进行post请求
def post_index(request):
    return render(request,'myblog/post_index.html')
#执行post请求
def post_do(request):
    username = request.POST.get("username")  #获取所有的id，返回都是一个list，如果没有，就返回空list
    pwd = request.POST.get("pwd")
    gender = request.POST.get("gender")
    love = request.POST.getlist("love")
    res_dic = {}
    res_dic["username"] = username
    res_dic["pwd"] = pwd
    res_dic["gender"] = gender
    res_dic["love"] = love
    return JsonResponse(res_dic)
#todo:get请求
def get_info(request):
    #http://127.0.0.1:8888/index/get_info/?id=123456&a=1&b=2&c=3&id=312
    # id = request.GET.get("id")  #如果有多个id，只会返回最后一个
    id = request.GET.getlist("id")  #获取所有的id，返回都是一个list，如果没有，就返回空list
    a = request.GET.get("a")
    b = request.GET.get("b")
    c = request.GET.get("c")
    res_dic = {}
    res_dic["id"] = id
    res_dic["a"] = a
    res_dic["b"] = b
    res_dic["c"] = c
    return JsonResponse(res_dic)
#todo:请求-HttpRequest
def req_info(request):
    #请求方法
    met = request.method #一个字符串，表示请求使用的HTTP 方法。常用值包括：'GET'、'POST
    #请求的url
    url = request.path #一个字符串，表示请求的页面的完整路径，不包含域名
    #编码方式
    encod = request.encoding #一个字符串，表示提交的数据的编码方式（如果为None 则表示使用DEFAULT_CHARSET设置，一般为utf-8）
    #请求人的ip
    addr_ip = request.META["REMOTE_ADDR"] #一个标准的Python字典，包含所有的HTTP头部。
    '''
        CONTENT_LENGTH —— 请求的正文的长度（是一个字符串）。
        CONTENT_TYPE —— 请求的正文的MIME 类型。 
        HTTP_ACCEPT —— 响应可接收的Content-Type。
        HTTP_ACCEPT_ENCODING —— 响应可接收的编码。
        HTTP_ACCEPT_LANGUAGE —— 响应可接收的语言。 
        HTTP_HOST —— 客服端发送的HTTP Host 头部。 
        HTTP_REFERER —— Referring 页面。 
        HTTP_USER_AGENT —— 客户端的user-agent 字符串。 
        QUERY_STRING —— 单个字符串形式的查询字符串（未解析过的形式）。 
        REMOTE_ADDR —— 客户端的IP 地址。 REMOTE_HOST —— 客户端的主机名。 
        REMOTE_USER —— 服务器认证后的用户。 
        REQUEST_METHOD —— 一个字符串，例如"GET" 或"POST"。 
        SERVER_NAME —— 服务器的主机名。 
        SERVER_PORT —— 服务器的端口（是一个字符串）。
    '''

    return HttpResponse(f"请求方法：{met} 请求的url：{url} 请求的编码方式：{encod} 请求的ip地址{addr_ip}")

#数据上下文传输
def var_test():
    return "羊驼老师真帅"
def val(request):
    conte = {"name111":"羊驼111",
             "name2":"久违",
             'list':["按你",'盖伦',"不知火舞"],
             'dic': {'nam1':"杰斯","sex":"男"},
             'var_test':var_test,
             }
    return render(request,'myblog/var.html',context=conte)

