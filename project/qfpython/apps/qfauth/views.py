from django.shortcuts import render
from django.contrib.auth import logout,login,authenticate
from django.views.generic import View
from .forms import LoginForm,RegisterForm
from django.views.decorators.http import require_POST,require_http_methods
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from utils import restful
User = get_user_model()
@require_POST
def register(request):
    form =RegisterForm(request.POST)
    if form.is_valid():
        telephone = form.cleaned_data.get('telephone')
        password = form.cleaned_data.get('password1')
        username = form.cleaned_data.get('username')
        #往数据库中存储
        user = User.objects.create_user(telephone=telephone,username=username,password=password)
        #存储成功 自动完成登录
        login(request,user)
        #返回成功的消息
        return restful.success()
    else:
        #获取表单错误信息
        errors = form.get_errors()
        print(errors)

        return restful.params_error(message=errors)


@require_http_methods(['GET','POST'])
def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        #实例化表单对象
        form = LoginForm(request.POST)
        if form.is_valid(): #如果符合表单验证要求
            #接收表单提交
            telephone = form.cleaned_data.get('telephone')
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')
            #验证用户名和密码
            user = authenticate(request,username=telephone,password=password)
            if user:
                if user.is_active:  #如果用户不是黑名单
                    login(request,user)
                    if remember:
                        #如果用户点击了记住我 那么让session永不过期
                        #默认的时间为14天
                        request.session.set_expiry(None)
                    else:
                        #否则会话结束就过期
                        request.session.set_expiry(0)
                    return restful.success()
                else:
                    return restful.unauth_error(message="您的账户被冻结了")
            else:
                return restful.params_error(message="手机号或者密码错误")
        else:
            errors = form.get_errors()
            return restful.params_error(message=errors)

