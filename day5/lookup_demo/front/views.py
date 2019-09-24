from django.shortcuts import render
from .models import Article,Category
from django.http import HttpResponse
from datetime import datetime,time
from django.utils.timezone import make_aware
# Create your views here.
def index(request):
    article = Article(title="琼琼孑立",content="彬彬有礼")

    category = Category(name="无码")
    category.save()
    article.category = category
    article.save()
    return HttpResponse("添加成功")


def index1(request):
    # article = Article.objects.get(pk=1)
    # print(article.query)
    # article = Article.objects.filter(title__exact="hello")
    # print(article.query)
    #查看最终执行的sql语句
    #但是只能是filter才能查看query  下面的get 用query会报错
    # article = Article.objects.get(id__exact=1)
    # print(article.query)
    article = Article.objects.filter(title__exact="hello")
    print(article.query)
    print(article)
    return HttpResponse("index1")

def index2(request):
    article = Article.objects.filter(title__contains="he")
    print(article.query)
    print(article)
    return HttpResponse("index2")

def index3(request):
    article = Article.objects.filter(title__icontains="hello")
    print(article.query)
    print(article)
    return HttpResponse("index3")

def index4(request):
    # articles = Article.objects.filter(id__in=[1,2])
    # for article in articles:
    #     print(article)

    # categorys = Category.objects.filter(article__in=[1,2])
    # ## 第一二篇文章的分类
    # for category in categorys:
    #     print(category)

    article = Article.objects.filter(title__icontains="hello")
    categories = Category.objects.filter(article__in=article)
    for category in categories:
        print(category)
    print(categories.query)

    return HttpResponse("index4")

def index5(request):
    article = Article.objects.filter(id__gt=1)
    print(article.query)
    print(article)
    return HttpResponse("index5")

def index6(request):
    article = Article.objects.filter(title__istartswith='琼')
    print(article.query)
    print(article)
    return HttpResponse("index6")

def index7(request):
    start_time = make_aware(datetime(year=2019,month=8,day=24,hour=12,minute=5,second=10))
    end_time = make_aware(datetime(year=2019,month=9,day=24,hour=23,minute=10,second=10))
    article = Article.objects.filter(create_time__range=(start_time,end_time))
    print(article.query)
    print(article)
    return HttpResponse("index7")

def index8(request):
    start_time = time(hour=2,minute=1,second=0)
    end_time = time(hour=23,minute=1,second=0)
    # article = Article.objects.filter(create_time__date=datetime(year=2019,month=8,day=24))
    # article = Article.objects.filter(create_time__year__gt=2018)
    article = Article.objects.filter(create_time__time__range=(start_time, end_time))
    print(article.query)
    print(article)
    return HttpResponse("index8")

def index9(request):
    # article = Article.objects.filter(create_time__isnull=True)
    article = Article.objects.filter(title__iregex=r"^h")
    print(article.query)
    print(article)
    return HttpResponse("index9")