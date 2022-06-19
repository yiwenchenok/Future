from django.contrib import admin
from .models import *
# Register your models here.



admin.site.register(Sentence)
admin.site.register(Tag)
admin.site.register(Comment)


#自定义注册
@admin.register(Post)  #注册方式2
class PostAdmin(admin.ModelAdmin):
    #在自定义列表页不能直接使用ManyToManyField字段,一对多和普通字段没有影响，在高版本的django中则没有问题
    list_display = ["title",'id','pub_time','modify_time','author_','tag_','classify','img']
    #列表页分页
    list_per_page = 50
    #过滤功能
    list_filter = ["title",'classify']
    #自定义详情页（编辑页）
    fieldsets = (
        ("标题/内容",{'fields':["title",'content']}),
        ("图片/来源/围观次数/点赞数/广告位",{'fields':["img",'source',"look","zan","adv"]}),
        ("分类",{'fields':["classify"]}),
        ("作者",{'fields':["author"]}),
        ("标签",{'fields':["tags"]}),
    )

    #搜索功能  外键字段需要通过两个下划线 两个下划线 两个下划线
    search_fields = ["title",'classify','author__username','tags__name','pub_time']