from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,Author,BookOrder,Publisher
from django.db.models import Avg,Count,Max,Min,Sum,F,Q
from django.db import connection
#获取所有图书的定价的平均价格
def index(request):
    result = Book.objects.aggregate(avg=Avg("price"))
    #相当于select avg(price) as avg from book;
    print(result)
    # print(result.query)报错 aggregate、get 都不能这样查看解析后的sql
    #aggregate 要通过connection 查看最终执行的sql语句
    print(connection.queries)
    return HttpResponse("index")

#获取每一本图书销售的平均价格
def index1(request):
    # result = Book.objects.aggregate(avg=Avg("bookorder__price"))
    result = Book.objects.annotate(avg=Avg("bookorder__price"))
    # print(result)
    for res in result:
        print('%s/%s' % (res.name,res.avg))
    print(connection.queries)
    return HttpResponse("index1")

def index2(request):
    #book表中总共多少本书
    #reslt = Book.objects.aggregate(booknums=Count("id"))
    #作者表中  多少个不同的邮箱 去重
    #result = Author.objects.aggregate(emailnum=Count('email',distinct=True))
    #每一本书的销量
    # result = Book.objects.annotate(booksales=Count("bookorder__book_id"))
    result = Book.objects.annotate(booksales=Count("bookorder"))
    #book_id默认是外键 可以不用写
    for res in result:
        print("%s/%s" % (res.name,res.booksales))
    print(connection.queries)
    return HttpResponse("index2")

def index3(request):
    #每一本书销售的时候最大价格和最小价格
    result = Book.objects.annotate(max=Max("bookorder__price"),min=Min("bookorder__price"))
    for res in result:
        print("%s/%s/%s" %(res.name,res.max,res.min))
    return HttpResponse("index3")

def index4(request):
    #所有图书销售的总额
    # result = BookOrder.objects.aggregate(total=Sum("price"))
    # print(result)

    #每一本书销售的总额
    # result = Book.objects.annotate(total=Sum("bookorder__price"))
    # for res in result:
    #     print("%s/%s" %(res.name,res.total))

    #2018年度销售总额
    # result = BookOrder.objects.filter(create_time__year=2018).aggregate(total=Sum("price"))
    # print(result)

    #每一本书2018年度销售的总额
    books = Book.objects.filter(bookorder__create_time__year=2018).annotate(total=Sum("bookorder__price"))
    for book in books:
        print("%s/%s" %(book.name,book.total))
    print(connection.queries)
    return HttpResponse("index4")

def index5(request):
    #每一本图书的售价 增加10块钱
    # books = Book.objects.all()
    # for book in books:
    #     book.price+=10
    #     book.save()
    # Book.objects.update(price=F("price")-10)
    # print(connection.queries[-1])
    #查询用户名和邮箱相等的 作者
    authors = Author.objects.filter(name=F("email"))
    for author in authors:
        print("%s/%s" %(author.name,author.email))
    print(connection.queries[-1])
    return HttpResponse("index5")


def index6(request):
    #价格大于95并且评分大于4.5
    # books = Book.objects.filter(price__gt=95,rating__gt=4.5)
    #books = Book.objects.filter(Q(price__gt=95)&Q(rating__gt=4.5))
    #如果需求是或者 办不了了
    #~表示取反
    books = Book.objects.filter(Q(price__gte=95)&~Q(name__icontains="传"))
    for book in books:
        print("%s/%s/%s" %(book.name,book.price,book.rating))
    return HttpResponse("index6")