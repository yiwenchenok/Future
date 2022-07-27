from django.db import models


# Create your models here.


#todo:1.自定义模型类管理器，重新定义objects
class MyBaseManager(models.Manager):
    def get_queryset(self):
        return super(MyBaseManager, self).get_queryset().filter(is_delete=False)   #返回未被逻辑删除的字段

class UserManager(MyBaseManager):
    def create(self,username,desc,age,height):
        my = self.model()  #self.model可以获取到对应的模型类实例对象
        my.username = username
        my.desc = desc
        my.age = age
        my.height = height
        return my



class User(models.Model):
    username = models.CharField(max_length=50, unique=True)  # 必选 参数max_length,unique字段只能是唯一值
    desc = models.TextField()  # 大文本字段，一般超过4000个字符时使用
    """
    这里同时定义了null和blank为True，这两个参数都是允许为空的意思，但是却是有区别的：
    null=True  表示在数据库层面允许为空。
    blank=True  表示在前端表单层面允许为空。
    """
    age = models.IntegerField(blank=True)  # 整数 blank：如果为True，则该字段允许为空白，
    height = models.FloatField(null=True)  # 浮点数 如果为True，表示允许为空
    # img = models.ImageField(upload_to='/person')
    create_time = models.DateTimeField(auto_now_add=True)  # auto_now_add表示当对象第一次被创建时自动设置当前时间，
    modify_time = models.DateTimeField(auto_now=True)  # 参数auto_now表示每次保存对象时，自动设置该字段为当前时间，用于"最后一次修改"的时间戳
    is_delete = models.BooleanField(default=False)  # default默认值

    def __str__(self):
        return self.username

    #todo:2.在模型类内部注册管理器
    yt_objects = UserManager() #默认就是 objects= models.Manager
