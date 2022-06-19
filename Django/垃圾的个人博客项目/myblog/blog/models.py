import os.path

from django.db import models
from DjangoUeditor.models import UEditorField
from django.contrib.auth.models import User
from myblog.settings import THUMB_DIR,MEDIA_ROOT,BASE_DIR
from PIL import Image  #pillow，常用的图片处理库
from django.db.models.fields.files import ImageFieldFile


def make_thumb(img_path,size=(80,60)):
    pix = Image.open(img_path).convert("RGB")
    pix.thumbnail(size) #压缩图片
    return pix


# Create your models here.
class Sentence(models.Model):
    """每日一句"""
    time = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=255)
    def __str__(self):
        return self.content
    class Meta:
        verbose_name_plural = "每日一句"

class Tag(models.Model):
    """标签"""
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "标签"

class Post(models.Model):

    title = models.CharField("标题",max_length=50)
    content = UEditorField("内容",width=800,height=600,imagePath='blog/')  #在内容中插入的图片上传的路径 media/blog
    img = models.ImageField() #图片,没有设置路径，则默认在media的根目录下
    thumb = models.ImageField(upload_to='thumb/') #缩略图
    pub_time = models.DateTimeField("创建时间",auto_now_add=True)
    modify_time = models.DateTimeField("修改时间",auto_now=True)
    source = models.CharField("来源", max_length=50)
    look = models.IntegerField("围观次数",default=0)
    zan = models.IntegerField("点赞数",default=0)
    adv = models.BooleanField("广告位",default=False)
    #分类
    choices = (
        ("网站前端","网站前端"),
        ("后端技术","后端技术"),
    )
    classify = models.CharField("分类",max_length=50,choices=choices)

    #外键关联
    author = models.ForeignKey(User) #作者
    def author_(self):
        return self.author.username
    author_.short_description = "作者"

    tags = models.ManyToManyField(Tag) #标签
    def tag_(self):
        return "/".join([i.name for i in self.tags.all()])
    tag_.short_description = "标签"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "文章"
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Post,self).save() #调用父类的save方法
        img_name,ext = os.path.splitext(os.path.basename(self.img.path))
        #获取上传的大图路径
        img_path = os.path.join(MEDIA_ROOT,self.img.name)
        #变成缩略图
        pix = make_thumb(img_path,size=(80,60))
        #构建缩略图保存的路径
        thumb_path = os.path.join(THUMB_DIR,img_name+"_thumb"+ext)
        pix.save(thumb_path)  #保存
        #路径保存django的格式，保存到数据库
        self.thumb = ImageFieldFile(self,self.thumb, thumb_path.split(BASE_DIR)[-1])
        super(Post, self).save()  # 调用父类的save方法



class Comment(models.Model):
    """评论表"""
    name = models.CharField(max_length=50,blank=False) #昵称
    email = models.CharField(max_length=50) #邮箱
    content = models.CharField(max_length=1000) #留言内容
    time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post) #关联文章

    class Meta:
        verbose_name_plural = "评论表"

















