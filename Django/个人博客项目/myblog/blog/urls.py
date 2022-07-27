from .views import *
from django.conf.urls import  url


urlpatterns = [
    # url("^index/",index,name='index'),
    # url("^detail/",detail,name='detail'),
    url("^zan/",zan,name='zan'),
    url("^comment/",comment,name='comment'),
    # url("^detail/",Detail.as_view(),name='detail'),
    url("^detail/",detail,name='detail'),
    url("^index/",Index.as_view(),name='index'), #类视图
    url("^$",index), #函数视图
]
