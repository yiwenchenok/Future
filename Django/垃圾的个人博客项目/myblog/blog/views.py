import time
from django.shortcuts import render,get_object_or_404
from .models import *
import random
from django.core.paginator import Paginator
from django.utils import timezone
from django.views.generic import ListView
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.db.models import Q
from haystack.generic_views import SearchView
# Create your views here.







#登录拦截器
def is_login(func):
    def inner(request,*args,**kwargs):
        if request.session.get('username'): #是登录状态
            return func(request,*args,**kwargs)
        else:
            return redirect('login')
    return inner





def comment(request):
    """评论功能"""
    commentName = request.POST.get("commentName")
    commentEmail = request.POST.get("commentEmail")
    commentContent = request.POST.get("commentContent")
    commentId = request.POST.get("commentId")
    try:
        #保存评论内容
        comment = Comment()
        comment.name = commentName
        comment.email = commentEmail
        comment.content = commentContent
        comment.post_id = commentId
        comment.save()

    except:
        pass
    finally:
        #获取到评论的文章所对应的所有评论
        detail_comment = Comment.objects.filter(post=commentId).order_by('-time')[:100]
        data_list = []
        #将评论数据构造成json
        for comm in detail_comment:
            dic = {}
            dic["name"] = comm.name
            dic["time"] = comm.time.strftime('%Y-%m-%d') #格式化时间： 年-月-日
            dic["content"] = comm.content
            data_list.append(dic)
        return JsonResponse({'data':data_list})




@csrf_exempt   #不进行csrf校验
def zan(request):
    """点赞功能"""
    try:
        id_ = request.POST.get("id")
        p = Post.objects.get(pk=id_)
    except Exception as e:
        return HttpResponse(e)
    else:
        #把时间撮写成session
        id_zan = request.session.get(id_+"zan",False)  #获取session,不同的文章，当点赞后就写入session
        if not id_zan or time.time() > id_zan:
            p.zan += 1
            p.save()
            #写入session，保存下次能点击的时间
            request.session[id_+"zan"] = time.time() + 24*60*60  #1天后才能点
            # request.session[id_+"zan"] = time.time() + 5
        return HttpResponse(p.zan)


def index(request):

    sen_all = Sentence.objects.all()
    sen = random.choice(sen_all)
    # p_list = Post.objects.all() #所有文章

    #获取分类
    classify = request.GET.get("classify","")
    if not classify:

        title = "首页"
        p_list = Post.objects.all()  # 所有文章
    elif classify == "1":
        title = "网站前端"
        p_list = Post.objects.filter(classify="网站前端")  # 所有分类为网站前端的文章
    else:
        title = "后端技术"
        p_list = Post.objects.filter(classify="后端技术")  # 所有分类为后端技术的文章
    #对所有文章分页
    p = Paginator(p_list,2) #两条数据一页
    page_num = request.GET.get("page",None)
    if not page_num:
        page_num = 1
    p_list = p.page(page_num)

    #本周热门
    time_now = timezone.now() #获取当前时间
    #确定当前是周几
    what_week_num = time_now.isoweekday() #返回的是一个数字，1代表周一，2代表周二
    #计算周一的时间
    time_monday = time_now - timezone.timedelta(days=what_week_num)
    #获取本周一到当前时间之内发布的所有文章,并根据look做降序排列，取前五篇
    hop_post = Post.objects.filter(pub_time__range=(time_monday,time_now)).order_by('-look')[:5]

    #历史热门推荐
    history_hop_post = Post.objects.all().order_by('-look')[:5]


    #广告位
    adv = Post.objects.filter(adv=True)


    conte = {
        "sen":sen,
        "p_list":p_list,
        "hop_post":hop_post,
        "classify":classify,
        "adv":adv,
        "history_hop_post":history_hop_post,
        "title":title,
    }


    return render(request,'index.html',context=conte)

class Index(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = "p_list"

    def get_queryset(self):
        return super(Index, self).get_queryset()

    def get_context_data(self, **kwargs):
        sen_all = Sentence.objects.all()
        sen = random.choice(sen_all)
        # p_list = Post.objects.all() #所有文章
        # 获取分类
        classify = self.request.GET.get("classify", "")
        if not classify:

            title = "首页"
            p_list = Post.objects.all()  # 所有文章
        elif classify == "1":
            title = "网站前端"
            p_list = Post.objects.filter(classify="网站前端")  # 所有分类为网站前端的文章
        else:
            title = "后端技术"
            p_list = Post.objects.filter(classify="后端技术")  # 所有分类为后端技术的文章
        # 对所有文章分页
        p = Paginator(p_list, 2)  # 两条数据一页
        page_num = self.request.GET.get("page", None)
        if not page_num:
            page_num = 1
        p_list = p.page(page_num)

        # 本周热门
        time_now = timezone.now()  # 获取当前时间
        # 确定当前是周几
        what_week_num = time_now.isoweekday()  # 返回的是一个数字，1代表周一，2代表周二
        # 计算周一的时间
        time_monday = time_now - timezone.timedelta(days=what_week_num)
        # 获取本周一到当前时间之内发布的所有文章,并根据look做降序排列，取前五篇
        hop_post = Post.objects.filter(pub_time__range=(time_monday, time_now)).order_by('-look')[:5]

        # 历史热门推荐
        history_hop_post = Post.objects.all().order_by('-look')[:5]

        # 广告位
        adv = Post.objects.filter(adv=True)

        conte = {
            "sen": sen,
            "p_list": p_list,
            "hop_post": hop_post,
            "classify": classify,
            "adv": adv,
            "history_hop_post": history_hop_post,
            "title": title,
        }
        return conte



class Detail(Index):
    model = Post
    template_name = 'content.html'

    def get_context_data(self, **kwargs):
        conte = super(Detail, self).get_context_data()

        id = self.request.GET.get("id")

        #获取到对应id的文章
        detai_post = get_object_or_404(Post,pk=id)
        #获取上一篇文章 python基础：索引会有越界，切片没有越界错误
        pre_post = Post.objects.filter(id__lt=id).order_by("-id")[:1]
        #获取下一篇文章
        next_post = Post.objects.filter(id__gt=id)[:1]

        conte["detail_post"] = detai_post
        conte["pre_post"] = pre_post
        conte["next_post"] = next_post

        return conte


class PostSerachView(SearchView):
    template_name = 'search/search.html'
    def get_context_data(self, **kwargs):
        conte = super(PostSerachView, self).get_context_data(**kwargs) #**kwargs不能省
        conte["page"] = conte
        sen_all = Sentence.objects.all()
        sen = random.choice(sen_all)
        # 历史热门推荐
        history_hop_post = Post.objects.all().order_by('-look')[:5]
        conte['sen'] = sen
        conte['history_hop_post'] = history_hop_post
        print(conte)
        return conte

@is_login #拦截器
def detail(request):
    sen_all = Sentence.objects.all()
    sen = random.choice(sen_all)
    #历史热门推荐
    history_hop_post = Post.objects.all().order_by('-look')[:5]
    conte = {
        "sen":sen,
        "history_hop_post":history_hop_post,
    }
    id = request.GET.get("id")
    # 获取到对应id的文章
    detai_post = get_object_or_404(Post, pk=id)
    # 获取上一篇文章 python基础：索引会有越界，切片没有越界错误
    pre_post = Post.objects.filter(id__lt=id).order_by("-id")[:1]
    # 获取下一篇文章
    next_post = Post.objects.filter(id__gt=id)[:1]
    #todo:相关推荐
    relation_post = Post.objects.filter(classify=detai_post.classify).exclude(id=detai_post.id).order_by("-look")[:8]
    # 基于标签做推荐
    tags = detai_post.tags.all()
    tag_post_list_all = []
    tag_post_list_all.extend(relation_post)  # 列表后追加一个列表
    random_post_list = []
    if tag_post_list_all:
        for i in range(8):
            post = random.choice(tag_post_list_all)
            if post not in random_post_list:
                random_post_list.append(post)
    for tag in tags:
        tag_post_list = tag.post_set.all()  # 通过一个标签对象，拿到关联的文章
        tag_post_list_all.extend(tag_post_list)  # 列表后追加一个列表
    conte["detail_post"] = detai_post
    conte["pre_post"] = pre_post
    conte["next_post"] = next_post
    conte["relation_post"] = random_post_list
    return render(request,"content.html",context=conte)









