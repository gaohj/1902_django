from django.http import HttpResponse
from django.shortcuts import render
from frontuser.models import FrontUser
from article.models import Article
# Create your views here.

def one_to_many_view(request):
    article = Article(title="钢铁是怎么练成的",content="所谓的浪漫是指你负责浪我负责漫")
    users = FrontUser(username="xcxk")

    users.save()
    article.author = users
    article.save()
    return HttpResponse("一对多添加数据成功")