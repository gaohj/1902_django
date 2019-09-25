from django.shortcuts import render
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
# Create your views here.
def index(request):
    print(type(request))
    return HttpResponse("首页")

def login(request):
    # print(request.path) #不包含域名端口号 参数
    # print(request.get_full_path())
    # print(request.META['REMOTE_ADDR']) #客户端 IP
    # print(request.is_secure()) #是否采用了https协议
    print(request.is_ajax()) #判断是否是ajax请求
    print(request.get_host()) #获取域名+端口号
    print(request.get_port()) #获取端口号
    print(request.get_raw_uri()) #获取完成的url
    print(request.COOKIES)
    return HttpResponse("登录页面")