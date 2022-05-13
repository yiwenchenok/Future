from django.db import models


# Create your models here.

class JDProductData(models.Model):
    product_id = models.CharField('商品ID', max_length=64)
    p_name = models.CharField('商品名', max_length=264, null=True, blank=True)
    p_price = models.FloatField('商品价格', default=0)
    p_imag_scr = models.CharField('商品图片', max_length=264, null=True, blank=True)
    p_shop = models.CharField('店铺名', max_length=264, null=True, blank=True)
    p_comment_count = models.CharField('评论数据', max_length=264, null=True, blank=True)
    p_sale = models.IntegerField('销量')
    p_pinpai = models.CharField('品牌', max_length=264, null=True, blank=True)
    p_detail = models.TextField('商品详情', null=True, blank=True)
    p_gender = models.CharField('性别', max_length=24, null=True, blank=True)

    class Meta:
        db_table = 'jd_product_data'
        verbose_name = 'JD商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.p_name
class user(models.Model):
    name = models.CharField(max_length=255)  # 账号
    password = models.CharField(max_length=255)
    def toDict(self):
        return {'id': self.id, 'username': self.name, }
    class Meta:
        db_table = "user"  # 更改表名