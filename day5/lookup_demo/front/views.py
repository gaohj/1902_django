from django.shortcuts import render
from .models import Article,Category
from django.http import HttpResponse
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