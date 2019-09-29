from django.shortcuts import render
from .forms import AddArticleForm
from django.http import HttpResponse
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
        return HttpResponse('success')
        #如果符合要求接收字段数据
    #不符合要求
    else:
        print(form.errors.get_json_data())
        return HttpResponse('faile')
        #进行相关处理

