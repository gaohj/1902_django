from django.shortcuts import render
from .models import Book,BookOrder,Author,Publisher
from django.http import HttpResponse
from django.db import connection
from django.db.models import F,Q,Count,Prefetch
from django.views.decorators.http import require_http_methods
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

def index7(request):
    books = Book.objects.all()
    print(connection.queries)
    for book in  books:
        print(book.name)
    print(connection.queries[-1])
    return HttpResponse("index7")

def index8(request):
    # books = Book.objects.defer('name')
    # for sql in connection.queries:
    #     print("+" * 50)
    #     print(sql)
    books = list(Book.objects.defer('name'))
    for sql in  connection.queries:
        print("+"*50)
        print(sql)
    #sql语句没有查询 name
    # books = Book.objects.defer('name')
    # #默认已经过滤掉了 name

    # for book in  books:
    #     print(book.name)
    #     print(type(book)) #defer返回的表示字典 而是模型
    #     # #但是你现在想要遍历 图书名字
    #     # #那么会重新向数据库发送一次查询 这次就有name了
    # for sql in  connection.queries:
    #     print("="*50)
    #     print(sql)
    return HttpResponse("index8")

def index9(request):
    books = Book.objects.only('name')
    for book in books:
        print('%s/%s' % (book.id,book.price))
    for sql in connection.queries:
        print("=" * 50)
        print(sql)
    return HttpResponse("index9")

def index10(request):
    book = Book.objects.get(id=1)
    print(book.id)
    print(connection.queries[-1])
    return HttpResponse("index10")


def index11(request):
    # publisher = Publisher(name="机械工业出版社")
    # publisher.save()
    # publisher = Publisher.objects.create(name="千锋教育出版社")
    # print(connection.queries[-1])
    # publisher = Publisher.objects.get_or_create(name="千锋扛把子出版社")
    # print(type(publisher))
    publisher = Publisher.objects.bulk_create([
        Publisher(name="彬彬出版社"),
        Publisher(name="琼琼出版社")
    ])
    print(connection.queries[-1])
    return HttpResponse("index11")

def index12(request):
    # res = Book.objects.filter(name="三国演义").exists()
    # print(res)
    # res = Book.objects.all()
    # print(len(res))
    res = Book.objects.count()
    print(res)
    return HttpResponse("index12")

def index13(request):
    # res = Book.objects.filter(name="三国演义").exists()
    # print(res)
    # res = Book.objects.all()
    # print(len(res))
    res = Book.objects.count()
    print(res)
    return HttpResponse("index13")

def index14(request):
    res = Book.objects.filter(bookorder__price__gte=85).order_by("bookorder__price").distinct()
    for book in res:
        print(book.name)
    print(connection.queries[-1])
    return HttpResponse("index14")

def index15(request):
    # books =Book.objects.all()
    # for book in books:
    #     book.price += 10
    #     book.save()
    # books = Book.objects.update(price=F("price")+5)
    orders = BookOrder.objects.filter(id__gte=6).delete()
    print(connection.queries[-1])
    return HttpResponse("index15")

def index16(request):
    # books =Book.objects.all()[1:2] #表示从1取到2 1 2表示索引    包括1 不包括2
    books =Book.objects.all()[1:] #表示从1取到末尾
    for book in books:
        print(book.name)
    print(connection.queries[-1])
    return HttpResponse("index16")