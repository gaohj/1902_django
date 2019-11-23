from django.shortcuts import render
from django.views.generic import View
from utils import restful
from django.views.decorators.http import require_GET,require_POST
import os
from django.conf import settings
from .forms import WriteNewsForm
from apps.news.models import NewsCategory,News
from django.core.paginator import Paginator
from datetime import datetime
from django.utils.timezone import make_aware
from urllib import parse
# Create your views here.
def index(request):
    return render(request,'cms/index.html')
class NewsList(View):
    def get(self,request):
        start = request.GET.get('start')
        end = request.GET.get('end')
        title = request.GET.get('title')

        category_id = int(request.GET.get('category',0) or 0)

        # 以上四个是用户想查询的条件


        page = int(request.GET.get('p',1))#用户想查看第几页
        newses = News.objects.select_related('category','author')

        if start or end:
            if start:
                start_date = datetime.strptime(start,'%Y/%m/%d')
            else:
                start_date = datetime(year=2016,month=11,day=11)
            if end:
                end_date = datetime.strptime(end,'%Y/%m/%d')
            else:
                end_date = datetime.today()
            newses = newses.filter(pub_time__range=(make_aware(start_date),make_aware(end_date)))
        if title:
            newses = newses.filter(title__icontains=title)
        if category_id:
            newses = newses.filter(category=category_id)


        paginator = Paginator(newses,2)
        page_obj = paginator.page(page)

        context_data = self.get_pagination_data(paginator,page_obj);
        context = {
            'categories':NewsCategory.objects.all(),
            'newses':page_obj.object_list,
            'page_obj':page_obj,
            'paginator':paginator,
            'start': start,
            'end': end,
            'title': title,
            'category': category_id,
            #为了防止查询的结果跳转页面丢失 所以我们需要拼接参数
            'url_query':'&'+parse.urlencode({
                'start':start or '',
                'end':end or '',
                'title':title or '',
                'category':category_id or ''
            })

        }
        context.update(context_data)
        return render(request,'cms/news_list.html',context=context)
    def get_pagination_data(self,paginator,page_obj,around_count=2):
        current_page = page_obj.number #获取当前页码
        num_pages = paginator.num_pages #总共有多少页

        left_has_more = False
        right_has_more = False

        if current_page <= around_count+2:
            left_pages = range(1,current_page)
        else:
            left_has_more = True
            left_pages = range(current_page-around_count, current_page)

        if current_page >= num_pages-current_page -1:

            right_pages = range(current_page+1, num_pages+1)
        else:
            right_has_more = True
            right_pages_pages = range(current_page+1, current_page+around_count+1)
        return {
            'left_pages':left_pages,
            'right_pages':right_pages,
            'current_page':current_page,
            'left_has_more':left_has_more,
            'right_has_more':right_has_more,
            'num_pages':num_pages
        }
    def post(self):
        pass

class WriteNewsView(View):
    def get(self,request):
        categories = NewsCategory.objects.all()
        context = {
            "categories": categories
        }
        return render(request,'cms/write_news.html',context=context)
    def post(self,request):
        form = WriteNewsForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            desc = form.cleaned_data.get('desc')
            thumbnail = form.cleaned_data.get('thumbnail')
            content = form.cleaned_data.get('content')
            category_id = form.cleaned_data.get('category')
            category = NewsCategory.objects.get(pk=category_id)
            News.objects.create(title=title,desc=desc,thumbnail=thumbnail,content=content,category=category)
            return restful.success()
        else:
            return restful.params_error(message=form.get_errors())

class EditNewsView(View):
    def get(self,request):
        news_id = request.GET.get('news_id')
        newses = News.objects.get(pk=news_id)
        categories = NewsCategory.objects.all()
        context = {
            'news':newses,
            "categories": categories
        }
        return render(request,'cms/write_news.html',context=context)
    def post(self,request):
        form = WriteNewsForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            desc = form.cleaned_data.get('desc')
            thumbnail = form.cleaned_data.get('thumbnail')
            content = form.cleaned_data.get('content')
            category_id = form.cleaned_data.get('category')
            category = NewsCategory.objects.get(pk=category_id)
            News.objects.create(title=title,desc=desc,thumbnail=thumbnail,content=content,category=category)
            return restful.success()
        else:
            return restful.params_error(message=form.get_errors())

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