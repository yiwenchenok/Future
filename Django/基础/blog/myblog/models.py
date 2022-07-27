from django.db import models
#todo:导入富文本编辑器
from DjangoUeditor.models import UEditorField
# Create your models here.
class Tag(models.Model):
    # 标签
    name = models.CharField("标签名",max_length=50)  # 标签名称

    def __str__(self):
        return self.name

    def myname(self):
        return self.name
    myname.short_description = "标签名"

    class Meta:
        verbose_name_plural = "标签"

class Category(models.Model):
    # 分类名
    category_name = models.CharField("分类名",max_length=20)  # char varchar
    def __str__(self):
        return self.category_name
    class Meta:
        verbose_name_plural = "分类"


class Post(models.Model):
    # 文章
    title = models.CharField(max_length=50)  # 标题
    # content = models.TextField('内容')  # 文章内容
    image = models.ImageField("封面",upload_to='myblog/')  # 封面保存为	myblog/yangtuo.png，但存储地址为： static/media/myblog/yangtuo.png，省略了static/media
    content = UEditorField(width=1000, height=600, imagePath='myblog/')  # 不需要重新迁移，UEditorField本身就是TextField的子类
    pub_time = models.DateTimeField('创建时间', auto_now_add=True)  # 时间,auto_now_add第一次自动添加，不允许修改，不能写到详情页
    #多对多
    tags = models.ManyToManyField(Tag,blank=True)  #标签
    #一对多
    category = models.ForeignKey(Category)

    def mytitle(self):
        return self.title
    mytitle.short_description = "标题"

    def mytag(self): #多对多字段：可以在list_play中注册，然后在admin后台列表页展示
        # return [i.name for i in self.tags.all()]
        return '/'.join([i.name for i in self.tags.all()])
    mytag.short_description = "标签"
    def category_name(self):
        return self.category
    category_name.short_description = "分类"
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "文章"







