from django.shortcuts import render
from django.views.generic import View
from apps.news.models import NewsCategory
from utils import restful
from django.views.decorators.http import require_GET,require_POST
import os
from django.conf import settings
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

def upload_file(request):
    file = request.FILES.get('file')
    filename = file.name
    with open(os.path.join(settings.MEDIA_ROOT,filename),'wb') as fp:
        for chunk in file.chunks():
            fp.write(chunk)
    url = request.build_absolute_uri(settings.MEDIA_URL+filename)
    return restful.result(data={'url':url})


import qiniu

@require_GET
def qntoken(request):
    access_key = settings.QINIU_ACCESS_KEY
    secret_key = settings.QINIU_SECRET_KEY
    q = qiniu.Auth(access_key, secret_key)

    bucket = settings.QINIU_BUCKET_NAME #存储空间
    token = q.upload_token(bucket)
    return restful.result(kwargs={"uptoken":token})