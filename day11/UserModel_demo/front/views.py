from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import User,Article
from django.views.generic import View
# from .models import Person
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import ContentType,Permission,Group
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
    # user = User.objects.get(pk=2)
    # print(user.has_perm('front.add_article'))
    user = User.objects.get(pk=2)
    # content_type = ContentType.objects.get_for_model(Article)  # 7
    # # 查看article模型有哪些权限
    # permissions = Permission.objects.filter(content_type=content_type)
    # for permission in permissions:
    #     user.user_permissions.add(permission)
    #     user.save()
    print(user.has_perm('front.add_article'))
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

class LoginView(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get('telephone')
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')
            user = authenticate(request,username=telephone,password=password)
            if user and user.is_active:
                login(request,user)
                if remember:
                    #None表示用户过期 默认的日期为14天
                    request.session.set_expiry(None)
                else:
                    request.session.set_expiry(0)
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect(reverse('index'))
            else:
                return HttpResponse("用户名或者密码错误")
        else:
            print(form.errors.get_json_data())
            return redirect(reverse('login'))
#自定义方法名坚决不能叫login 和logout 系统系统了这个方法  防止冲突
def my_logout(request):
    logout(request)
    return redirect(reverse('index'))

# @login_required(login_url='/login/')
# print(reverse('login'))
# test = reverse('login')
@login_required(login_url='/login/')
def list(request):
    return HttpResponse("测试")

def add_permission(request):
    #所有的模型都在 content_type表中
    #给模型添加权限 第一步先要找到 指定的模型
    content_type = ContentType.objects.get_for_model(Article) #返回Article模型对应的 content_type id
    permission = Permission.objects.create(content_type=content_type,codename="black article",name='拉黑文章')
    return HttpResponse("权限创建成功")

def operate_permission(request):
    #查找用户
    user = User.objects.first()
    #想让用户操作哪个模型  先查出模型的id
    content_type = ContentType.objects.get_for_model(Article) #7
    #查看article模型有哪些权限
    permissions = Permission.objects.filter(content_type=content_type)
    for permission in permissions:
        pass
        # print(permission)
        # user.user_permissions.add(permission)
        # user.save()
        # user.user_permissions.remove(permission)
        # user.save()
    # user.user_permissions.set(permissions)
    # user.user_permissions.remove(*permissions)
    # user.save()
    # if user.has_perm('front.black_article'):
    #     print("拥有这个权限")
    # else:
    #     print("没有这个权限")
    print(user.get_all_permissions())
    return HttpResponse("给用户添加权限")
@permission_required(['front.add_article','front.view_article'],login_url='/login/')
def add_article(request):

    return HttpResponse("添加文章页面")


def operate_group(request):
    # group = Group.objects.create(name="运营")
    # group.save()
    # groups = Group.objects.first()
    # content_type = ContentType.objects.get_for_model(Article)  # 7
    # permissions = Permission.objects.filter(content_type=content_type)
    # groups.permissions.set(permissions)
    # groups.save()
    groups = Group.objects.filter(name="运营").first()
    user = User.objects.get(pk=2)
    user.groups.add(groups)
    user.save()
    return HttpResponse("操作分组的视图函数")

