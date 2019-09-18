from django.http import HttpResponse
from django.shortcuts import redirect,reverse
# Create your views here.

def index(request):
    username = request.GET.get('username')
    if username:
        return HttpResponse("前台首页")
    else:
        # return redirect('/signin/')
        login_url = reverse('front:login')
        print("="*50)
        print(login_url)
        print("="*50)
        return redirect(login_url)

def login(request):
    return HttpResponse("前台登录页")
