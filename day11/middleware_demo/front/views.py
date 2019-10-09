from django.shortcuts import render,redirect,reverse
from django.views.generic import View
from .models import User
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.front_user:
        print(request.front_user.username)
    return render(request,'index.html')

def lists(request):
    if request.front_user:
        print(request.front_user.username)
    return HttpResponse("my list")

class SigninView(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username,password=password).first()
        if user:
            request.session['user_id'] = user.id
            return redirect(reverse('index'))
        else:
            messages.info(request,'用户名或者密码错误')
            return redirect(reverse('login'))
