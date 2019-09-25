from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
# Create your views here.

def index(request):
    username = request.GET.get('username')
    if username:
        return HttpResponse("首页")
    else:
        return redirect(reverse('signup'))


def signup(request):
    return HttpResponse("注册页面")