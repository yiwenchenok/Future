from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
import re
from .models import User
from django.shortcuts import HttpResponseRedirect
# Create your views here.

class Reg(View):
    def get(self,request):
        return render(request,'login/reg.html')
    def post(self,request):
        username = request.POST.get('username')
        cpassword = request.POST.get('cpassword')
        password = request.POST.get('password')

        if not all([username,password,cpassword]):
            return JsonResponse({'code':0,'msg':"有必填未填写"})

        if username.isdigit():
            return JsonResponse({'code': 0, 'msg': "账号不能全为数字"})

        if len(username) > 8:
            return JsonResponse({'code': 0, 'msg': "账号长度必须小于8"})

        if not re.match("[0-9a-zA-Z]{4,16}",password):
            return JsonResponse({'code': 0, 'msg': "密码必须为4-16位数字或字母"})

        if password != cpassword:
            return JsonResponse({'code': 0, 'msg': "两次输入的密码不一致"})

        try:
            #写入数据库
            u = User(username=username,password=password)
            u.save()
        except:
            return JsonResponse({'code': 0, 'msg': "用户名已经被占用"})

        return JsonResponse({'code': 1, 'msg': "注册成功",'url':'/login/','username':username,'pwd':password})

class Login(View):
    def get(self,request):
        return render(request,'login/login.html')

    def post(self,request):
        username = request.POST.get('username')

        password = request.POST.get('password')

        if not all([username,password]):
            return JsonResponse({'code':0,'msg':"有必填未填写"})

        #判断用户是否存在
        user = User.objects.filter(username=username).first()
        if not user:
            return JsonResponse({'code': 0, 'msg': "账号未注册"})
        if user.password != password:
            return JsonResponse({'code': 0, 'msg': "账号或者密码错误"})

        #登录成功
        request.session.flush()  #将之前登录的账号下线
        request.session["username"] = user.username  #记录登录状态
        request.session.set_expiry(24*60*60)  #超时时间 s

        return JsonResponse({'code': 1, 'msg': "登录成功",'url':'/'})



def switcher(request):
    """切换用户"""
    if "username" in request.session.keys():
        #删除session值
        del request.session["username"]

    return HttpResponseRedirect("/login")












