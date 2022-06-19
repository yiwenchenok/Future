from django.db import models
from datetime import datetime
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=16,unique=True)
    password = models.CharField(max_length=40)
    is_delete = models.BooleanField(default=False)
    create_time = models.DateTimeField(default=datetime.now)
    class Meta:
        verbose_name_plural = "用户"