from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.

def index(request):
    # user = User.objects.create_user(username="kangbazi",email="jiabin@qq.com",password="123456")
    # user = User.objects.create_superuser(username="superman1",email="superman1@qq.com",password="123456")
    # user.last_name = '666'
    # user.first_name = 'kangbazi'
    # user = User.objects.get(pk=2)
    # user.set_password('654321')
    # user.save()
    username = 'kangbazi'
    password = '123456'
    user = authenticate(request,username=username,password=password)
    if user:
        print("%s登录成功"% user.username)
    else:
        print("用户名或者密码错误")
    return render(request,'index.html')

