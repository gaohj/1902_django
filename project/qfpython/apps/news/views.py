from django.shortcuts import render
from django.http import HttpResponse
from .models import News,NewsCategory
from django.conf import settings
from utils import restful
from .serializers import NewsSerializers,CommetSerializers
from django.http import Http404
from .forms import PublicCommentForm
from .models import Comments
# Create your views here.
def index(request):
    count = settings.ONE_PAGE_NEWS_COUNT
    newses = News.objects.select_related('category','author').all()[0:count]
    categories = NewsCategory.objects.all()
    context = {
        'newses':newses,
        'categories':categories,
    }
    return render(request,'news/index.html',context=context)

def news_list(request):
    #通过p参数 指定获取第几页的数据 /news/list/?p=2
    page = int(request.GET.get('p',1))
    category_id = int(request.GET.get('category_id',0))
    # 1 0,2  01
    # 2 2,4  23
    # 3 4,6  45
    start = (page-1)*settings.ONE_PAGE_NEWS_COUNT
    end = start+settings.ONE_PAGE_NEWS_COUNT
    if category_id == 0:
        newses = News.objects.select_related('category','author').all()[start:end]
    else:
        newses = News.objects.select_related('category','author').filter(category__id=category_id)[start:end]
    serializer = NewsSerializers(newses,many=True)#每一条数据都要序列化
    data = serializer.data
    return restful.result(data=data)


def news_detail(request,news_id):
    try:
        newses = News.objects.select_related('category','author').get(pk=news_id)
        context = {
            'news':newses
        }
        return render(request,'news/news_detail.html',context=context)
    except News.DoesNotExist:
        raise Http404

def public_comment(request):
    form = PublicCommentForm(request.POST)
    if form.is_valid():
        news_id = form.cleaned_data.get('news_id')
        content = form.cleaned_data.get('content')
        news = News.objects.get(pk=news_id)
        #往数据库中添加
        comment = Comments.objects.create(content=content,author=request.user,news=news)
        serializer = CommetSerializers(comment)
        return restful.result(data=serializer.data)
    else:
        return restful.params_error(message=form.get_errors())


