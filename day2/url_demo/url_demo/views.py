from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'index.html')

def login(request):
    next = request.GET.get('next')
    text = "登录页面,登录完成以后要跳转的页面是:%s" % next
    return HttpResponse(text)

def book_detail(request,book_id,category):
    text = "您要查询的id是:%s，分类是:%s" % (book_id,category)
    return HttpResponse(text)