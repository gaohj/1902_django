from django.http import HttpResponse

def article(request):
    return HttpResponse("文章首页")

def article_list(request,categories):
    text = "您填写的分类是:%s" % categories
    return HttpResponse(text)