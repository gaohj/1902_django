from django.shortcuts import render
from .forms import AddArticleForm,RegisterForm
from django.http import HttpResponse
from django.views.decorators.http import require_POST
#导入表单
# Create your views here.
def add_article(request):
    #这里实例化表单对象
    form = AddArticleForm(request.POST)
    #判断是否符合要求
    #if 判断
    if form.is_valid():
        title = form.cleaned_data.get('title')
        content = form.cleaned_data.get('content')
        word_num = form.cleaned_data.get('word_num')
        price = form.cleaned_data.get('price')
        print(title,content,word_num,price)
        form.save()
        #要求在clean 没有问题之后才能调用  之前调用会抛出异常
        #
        return HttpResponse('success')
        #如果符合要求接收字段数据
    #不符合要求
    else:
        print(form.errors.get_json_data())
        return HttpResponse('faile')
        #进行相关处理

@require_POST
def register(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        # 要求在clean 没有问题之后才能调用  之前调用会抛出异常
        #commit=False只会生成模型的对象  不会把它真正的插入到数据库中
        #其它字段补充完成以后 再插入到数据库
        user = form.save(commit=False)
        user.password = form.cleaned_data.get('pwd1')
        user.save()
        #
        return HttpResponse('success')
    else:
        print(form.errors.get_json_data())
        return HttpResponse('fail')
