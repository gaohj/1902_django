from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .models import Article
from .forms import ArticleForm
# Create your views here.

class IndexView(View):
    def get(self,request):
        return render(request,'index.html')
    # def post(self,request):
    #     myfile = request.FILES.get('myfile')
    #     with open('files/somefile.jpg','wb') as fp:
    #         for chunk in myfile.chunks():
    #             fp.write(chunk)
    #     return HttpResponse('success')
    # def post(self,request):
    #     title = request.POST.get('title')
    #     content = request.POST.get('content')
    #     file = request.FILES.get('myfile')
    #     print(file)
    #     Article.objects.create(title=title,content=content,thumbnail=file)
    #     return HttpResponse('success')
    def post(self,request):
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('success')
        else:
            print(form.errors.get_json_data())
            return HttpResponse('fail')

