from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import User
# from .models import Person
from django.http import HttpResponse
# Create your views here.

def index(request):
    #user = User.objects.create_user(username="blackman",email="blackman@qq.com",password="123456")
    #user = User.objects.create_superuser(username="superman1",email="superman1@qq.com",password="123456")
    #user.last_name = '888'
    #user.first_name = 'jiabin'
    # user = User.objects.get(pk=2)
    # user.set_password('654321')
    #user.save()
    # username = 'kangbazi'
    # password = '123456'
    # user = authenticate(request,username=username,password=password)
    # if user:
    #     print("%s登录成功"% user.username)
    # else:
    #     print("用户名或者密码错误")
    #user = User.objects.create_user(telephone='18777777777',username='qiongqiong',password="123456",email='qiongqiong@163.com')
    return render(request,'index.html')

def proxy_view(request):
#     blacklist = Person.get_black_list()
#     for person in blacklist:
#         print(person.username)
     return HttpResponse("Person是User模型的代理模型实际上是User在执行")

def my_authenticate(telephone,password):
    user = User.objects.filter(extension__telephone=telephone).first()
    if user:
        is_correct = user.check_password(password)
        if is_correct:
            return user
        else:
            return None
    else:
        return None


def one_to_one(request):
    # user = User.objects.create_user(username="qiongqiong",email="qiongqiong@126.com",password="123456")
    # user.extension.telephone = '18888888888'
    # user.extension.school = '上海交大'
    # user.save()
    telephone =  request.GET.get('telephone')
    password = request.GET.get('password')
    user = my_authenticate(telephone,password)
    if user:
        print("%s验证成功"%user.username)
    else:
        print("%s验证失败" % user.username)
    return HttpResponse("一对一扩展用户模型")

def inherit_view(request):
    telephone = '18777777799'
    password = '123456'
    username = 'aqiong'
    email = 'aqiong@vip.qq.com'
    # user = authenticate(request,username=telephone,password=password)
    # if user:
    #     print(user.username)
    #     print("验证成功")
    # else:
    #     print("验证失败")
    user = User.objects.create_superuser(telephone=telephone,username=username,password=password,email=email)
    print(user.username)

    return HttpResponse("继承自AbstractUser模型")

def inheritbase_view(request):
    telephone = '18777777799'
    password = '123456'
    username = 'aqiong'
    email = 'aqiong@vip.qq.com'
    user = authenticate(request,username=telephone,password=password)
    if user:
        print(user.username)
        print("验证成功")
    else:
        print("验证失败")
    # user = User.objects.create_superuser(telephone=telephone,username=username,password=password,email=email)
    # print(user.username)

    return HttpResponse("继承自AbstractBaseUser模型")