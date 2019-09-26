
from django.shortcuts import render
from django.views.decorators.http import require_GET,require_safe,require_POST,require_http_methods
from .models import Aricle
from django.http import HttpResponse
from django.views.generic import View
@require_GET
def add_article(request):
    articles = []
    for x in range(0,200):
        article = Aricle(title="标题:%s" % x,content="内容:%s" % x)
        articles.append(article)
    Aricle.objects.bulk_create(articles)

    return HttpResponse("文章添加成功")

class AddArticleView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'add_article.html')
    def post(self,request,*args,**kwargs):
        book_name = request.POST.get('name')
        book_content = request.POST.get('content')
        print("name:{},content:{}".format(book_name,book_content))
        return HttpResponse("success")


class ArticleDetail(View):
    def get(self,request,article_id):
        print("文章的id是:%s" % article_id)
        return HttpResponse("success")
    #不管什么请求 都会走这个方法
    def dispatch(self, request, *args, **kwargs):
        print("不管什么方式请求我都走这里")
        return super(ArticleDetail, self).dispatch(request, *args, **kwargs)
    #上面只允许get 请求  其它请求 都会给反馈 不支持
    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse("不支持get以外其他的请求")

