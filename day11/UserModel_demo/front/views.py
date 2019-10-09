from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
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

