from django.http import HttpResponse
from django.shortcuts import render
from frontuser.models import FrontUser,UserExtension
from article.models import Article,Tag
# Create your views here.

def one_to_many_view(request):
    article = Article(title="钢铁是怎么练成的",content="所谓的浪漫是指你负责浪我负责漫")
    users = FrontUser(username="xcxk")

    users.save()
    article.author = users
    article.save()
    return HttpResponse("一对多添加数据成功")

def one_to_one_view(request):
    #先查到第一个用户
    # user = FrontUser.objects.first()
    # extension = UserExtension(cardid=123456789123456789)
    # extension.user = user
    # extension.save()
    extension = UserExtension.objects.first()
    print(extension.user) #<FrontUser:(id:1,username:xcxk)>
    return HttpResponse("一对一添加数据成功")

def many_to_many_view(request):
    # article = Article(title="钢铁是怎么样练成的",content="你负责浪我负责慢")
    # article.save()
    # tag = Tag(name="冷门")
    # tag.save()
    #
    # tag.articles.add(article) 这是 把ManyToManyField 写到 tag模型上

    article = Article.objects.first()

    tag = Tag(name="热门")
    tag.save()
    article.tag_set.add(tag)#这是 把ManyToManyField 写到 Article模型上 
    return HttpResponse("多对多添加数据成功")




