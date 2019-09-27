from django.shortcuts import render
from django.views.generic import View
from .forms import MyForm,RegisterForm
from django.http import HttpResponse
from .models import User
# Create your views here.




class IndexView(View):
    def get(self,request):
        form = MyForm()
        return render(request,'index.html',context={"form":form})
    def post(self,request):
        form = MyForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            price = form.cleaned_data.get('price')
            personal_website = form.cleaned_data.get('personal_website')

            print(email,price,personal_website)
            return HttpResponse("首页")
        else:
            print(form.errors.get_json_data())
            return HttpResponse("失败")

class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            telephone = form.cleaned_data.get('telephone')
            User.objects.create(username=username,telephone=telephone)
            return HttpResponse("注册成功")
        else:
            #{'telephone': [{'message': '13888888888已经被注册', 'code': ''}]}
            # print(form.errors.get_json_data())
            print(form.get_errors())
            return HttpResponse("失败")
