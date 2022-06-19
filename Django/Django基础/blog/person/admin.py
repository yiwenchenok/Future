from django.contrib import admin
from .models import User
# Register your models here.

# admin.site.register(User)

@admin.register(User)
class MyUserAdmin(admin.ModelAdmin):
    list_display = ["username",'id','age','height','is_delete','create_time','modify_time']