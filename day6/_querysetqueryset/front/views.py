from django.shortcuts import render
from .models import Book,BookOrder,Author,Publisher
from django.http import HttpResponse
from django.db import connection
from django.db.models import F,Q,Count,Prefetch
# Create your views here.
def index(request):
    print(type(Book.objects))
    books = Book.objects.filter(id__gt=1).all()

    for book in books:
        print("%s" % book.name)
    print(connection.queries[-1])
    return HttpResponse("index")

def index1(request):
    # books = Book.objects.filter(id__gte=1).exclude(id=2)
    # for book in books:
    #     print("%s" % book.name)
    books = Book.objects.annotate(author_name=F("author__name"))
    for book in books:
        print("%s/%s" % (book.name,book.author_name))
    print(connection.queries[-1])
    return HttpResponse("index1")

def index2(request):
    # orders = BookOrder.objects.order_by("create_time")
    # orders = BookOrder.objects.order_by("-create_time")
    # orders = BookOrder.objects.order_by("-create_time","-price")
    #这种情况下  如果create_time生效了  后面price 自动忽略
    # orders = BookOrder.objects.order_by("-book__rating")
    # orders = BookOrder.objects.order_by("-create_time").order_by("-price")
    # #后边的order_by 会把前面的 order_by 打乱
    # for order in orders:
    #     print("%s/%s/%s" % (order.id,order.price,order.create_time))
    #提取图书数据 根据图书的销量进行排序
    books = Book.objects.annotate(xiaoliang=Count("bookorder")).order_by("-xiaoliang")
    for book in books:
        print("%s/%s" % (book.name,book.xiaoliang))
    return HttpResponse("index2")

def index3(request):
    # books = Book.objects.values("id","name",authors=F("author__name")) #返回的是字典
    # books = Book.objects.values("id","name",dingdan=Count("bookorder"))
    # books = Book.objects.values_list("id","name") #values_list 返回的是元祖
    books = Book.objects.values_list("name") #values_list 返回的是元祖
    #<QuerySet [('三国演义',), ('水浒传',), ('西游记',), ('红楼梦',)]>
    books = Book.objects.values_list("name",flat=True)
    #<QuerySet ['三国演义', '水浒传', '西游记', '红楼梦']> 结果扁平化 前提是只有一个字段才能用
    # print(type(books))
    # # for book in books:
    # #     for key,value in book.items():
    # #         print(key)
    # for book in books:
    #     print(type(book))
    print(books)
    print(connection.queries[-1])
    return HttpResponse("index3")

def index4(request):
    books = Book.objects.all()
    print(books)
    #<QuerySet [<Book: Book object (1)>, <Book: Book object (2)>, <Book: Book object (3)>, <Book: Boo
   #k object (4)>]>
    for book in books:
        print(book.name)
    print(connection.queries[-1])
    return HttpResponse("index4")

#select_related 提取某个模型的同时  将关联的模型的数据也提取出来 比如文章  提取文章的同时将作者也拿出来
#以后用到 article.author 就不用再去访问数据库了
def index5(request):
    books = Book.objects.select_related("author","publisher")
    #select_related只能用在 一对多 一对一 不能用在 多对多 多对一
    #我们可以使用select_related  来提前获取文章的作者 但是不能通过 作者 提前获取作者的文章
    #不能提前获取文章的 所有标签
    #查询图书的同时 将作者出版社信息也取出来
    #下次我们用book.author.name 不需要再去请求数据库了
    for book in books:
        print(book.author.name) #
        print(book.publisher.name)
    print(connection.queries[-1])
    return HttpResponse("index5")
#prefetch_related 弥补select_related 不足 实现 多对多 多对一
#满足所有的表关系
#我想获取 标题中带有 佳彬的 文章以及文章所有的标签
def index6(request):
    # books = Book.objects.prefetch_related("bookorder_set")
    # for book in books:
    #     print("="*50) #
    #     print(book.name)
    #     orders = book.bookorder_set.all()
    #     for order in orders:
    #         print(order.id)
    # books = Book.objects.prefetch_related("author")
    # for book in books:
    #     print(book.author.name)
    # print(connection.queries[-1])
    #查询图书的订单  想要在查询订单的时候指定过滤条件
    prefetch = Prefetch("bookorder_set",queryset=BookOrder.objects.filter(price__gte=93))
    books = Book.objects.prefetch_related(prefetch)
    for book in books:
        print("="*50) #
        print(book.name)
        orders = book.bookorder_set.all()
        for order in orders:
            print(order.id)
    print(connection.queries[-1])
    return HttpResponse("index6")
