from django.contrib import admin
from .models import Tag,Category,Post #导入定义模型类

# Register your models here.

#todo:注册模型类

# admin.site.register(Tag)
# admin.site.register(Category) #默认方式
# admin.site.register(Post) #默认方式

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['myname', 'id']

#内嵌的模型类需要继承admin.Stack
# class PostInline(admin.StackedInline): #竖直的
class PostInline(admin.TabularInline): #水平的
    model = Post
    extra = 3

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name','id']

    #声明内嵌的模型类 （一对多的多）
    inlines =  [PostInline]



#自定义注册
# admin.site.register(Post,PostAdmin) #自定义注册方式1
@admin.register(Post)  #自定义注册方式2
class PostAdmin(admin.ModelAdmin):
    #在自定义列表页不能直接使用ManyToManyField字段,一对多和普通字段没有影响，在高版本的django中则没有问题
    list_display = ["mytitle",'id','content','pub_time','mytag','category_name']
    #列表页分页
    list_per_page = 3
    #过滤功能
    list_filter = ["title",'category','tags']

    #自定义详情页（编辑页）
    fieldsets = (
        ("标题/正文",{'fields':["title",'content']}),
        ("标签/分类",{'fields':["tags",'category']}),
    )
    #搜索功能  外键字段需要通过两个下划线 两个下划线 两个下划线
    search_fields = ["title",'category__category_name','content']



