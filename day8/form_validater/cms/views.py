from django.shortcuts import render
from django.views.generic import View
from .forms import MyForm
from django.http import HttpResponse
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