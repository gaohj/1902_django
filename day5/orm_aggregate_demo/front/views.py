from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,Author,BookOrder,Publisher
from django.db.models import Avg,Count,Max,Min,Sum
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