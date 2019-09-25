from django.shortcuts import render
from .models import Article
from django.views.decorators.http import require_http_methods,require_GET,require_POST,require_safe
from django.http import HttpResponse
# Create your views here.
# @require_http_methods(['GET'])
#@require_GET = @require_http_methods(['GET'])
@require_GET
def index(request):
    articles = Article.objects.all()
    return render(request,'index.html',context={"articles":articles})
@require_http_methods(['GET','POST'])
def add_article(request):
    if request.method == 'GET':
        return render(request,'add_article.html')
    else:
        title = request.POST.get('title')
        content = request.POST.get('content')
        price = request.POST.get('price')
        Article.objects.create(title=title,content=content,price=price)
        return HttpResponse("success")
@require_safe
def hello(request):
    return HttpResponse("我只允许相对安全的请求方式来访问视图")
#get head 这两个都是进行查看  并没有增删改的操作