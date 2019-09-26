
from django.shortcuts import render
from django.views.decorators.http import require_GET,require_safe,require_POST,require_http_methods
from .models import Aricle
from django.http import HttpResponse
from django.views.generic import View,TemplateView,ListView
from django.core.paginator import Paginator,Page
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

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        context['name']='guodongxiong'
        return context

class ArticleListView(ListView):
    model = Aricle
    template_name = 'article_list1.html'
    context_object_name = 'articles'
    paginate_by = 10
    ordering = 'create_time'
    page_kwarg = 'p'

    def get_context_data(self,**kwargs):
        context = super(ArticleListView, self).get_context_data()
        paginator = context.get('paginator') #拿到 Paginator 对象
        # print("====")
        # print(paginator)
        page_obj = context.get('page_obj') #拿到Page 对象
        # print("%%%%%")
        # print(page_obj)
        pagination_data = self.get_pagination_data(paginator,page_obj,2)
        context.update(pagination_data)
        return context
    def get_pagination_data(self,paginator,page_obj,around_count=3):
        #获取当前页码
        current_page = page_obj.number
        num_pages = paginator.num_pages #总共有多少页

        left_has_more = False
        right_has_more = False
        # 3 <= 3+2
        #range(1,3)
        #如果当前页码小于5  不能出现 ...而是展示左边所有的页码
        if current_page <= around_count+2:
            left_pages = range(1,current_page)
        else:
            left_has_more = True
            #8
            #(5,8)  展示567   上一页1...567891011...下一页
            left_pages = range(current_page-around_count,current_page)

        if current_page >= num_pages-around_count-1:
            # 不如  当前第17页
            #17 18 19 20
            #range 应该从下一页开始取 因为还要取到20   range(18,21)
            #如果range(18,20) 只能去掉第19页 取不到20 所以 +1
            right_pages = range(current_page+1,num_pages+1)
        else:
            right_has_more = True
            #比如12
            #       ....9 10 11 12 13 14 15...20
            #range(13,12+3+1)
            right_pages = range(current_page+1,current_page+around_count+1)

        return {
            'left_pages':left_pages,
            'right_pages':right_pages,
            'current_page':current_page, #当前页码
            'left_has_more':left_has_more,
            'right_has_more':right_has_more,
            'num_pages':num_pages #总共多少页
        }