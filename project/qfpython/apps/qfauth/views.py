from django.shortcuts import render,redirect,reverse
from django.contrib.auth import logout,login,authenticate
from django.views.generic import View
from .forms import LoginForm,RegisterForm
from django.views.decorators.http import require_POST,require_http_methods
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from utils import restful,aliyunsms
from utils.captcha.xfzcaptcha import Captcha
from django.core.cache import cache
from io import BytesIO
User = get_user_model()
@require_POST
def register(request):
    form =RegisterForm(request.POST)
    if form.is_valid():
        telephone = form.cleaned_data.get('telephone')
        password = form.cleaned_data.get('password1')
        username = form.cleaned_data.get('username')
        print(telephone,username,password)
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
            print(telephone)
            password = form.cleaned_data.get('password')
            print(password)
            remember = form.cleaned_data.get('remember')
            print(remember)
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

def sms_captcha(request):
    #接收手机号
    telephone = request.GET.get('telephone')
    #生成随机验证码
    code = Captcha.gene_text() #调用captcha文件夹中的 Captcha类中的 gene_text方法 完成随机验证码
    #将验证码 放到memcached中 或者 session中
    cache.set(telephone,code,5*60)
    print(code)
    result = aliyunsms.send_sms(telephone,code)
    return restful.success()

def img_captcha(request):
    text,image = Captcha.gene_code() #从验证码类的类方法 获取text和 image  不能直接放到HttpResponse返回
    #因为是图片 也就是流数据 需要单独的存储
    out = BytesIO()
    #调用image的save方法  将image对象保存在BytesIO
    image.save(out,'png')

    #当image对象进入BytesIO后 指针从0 到1 后期需要读取保存到response对象上面 如果从1往后读，肯定读取不到1
    #需要从指针播到0
    out.seek(0)
    response = HttpResponse(content_type='image/png')
    response.write(out.read()) #从BytesIO读取数据  保存到response对象上
    response['Content-length'] = out.tell()
    cache.set(text.lower(),text.lower(),5*60)
    print(cache.get(text.lower()))
    return response

def logout_view(request):
    logout(request)
    return redirect(reverse('index'))