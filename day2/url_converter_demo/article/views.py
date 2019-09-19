from django.http import HttpResponse
from django.shortcuts import reverse

def article(request):
    return HttpResponse("文章首页")

def article_list(request,categories):
    print("categories:%s" % categories)
    print(reverse('list',kwargs={'categories':categories}))
    text = "您填写的分类是:%s" % categories
    return HttpResponse(text)