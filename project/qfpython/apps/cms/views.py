from django.shortcuts import render
from django.views.generic import View
from apps.news.models import NewsCategory
from utils import restful
# Create your views here.
def index(request):
    return render(request,'cms/index.html')

class WriteNewsView(View):
    def get(self,request):
        categories = NewsCategory.objects.all()
        context = {
            "categories": categories
        }
        return render(request,'cms/write_news.html',context=context)
    def post(self):
        pass

def news_category(request):
    categories = NewsCategory.objects.all()
    context = {
        "categories":categories
    }
    return render(request,'cms/news_category.html',context=context)
def add_news_category(request):
    name = request.POST.get('name') #从前端接收分类 名称
    exists = NewsCategory.objects.filter(name=name).exists()
    if not exists:
        NewsCategory.objects.create(name=name)
        return restful.success()
    else:
        return restful.params_error(message="该分类已经存在")