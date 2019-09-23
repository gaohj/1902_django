from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.

def index(request):
    # book = Book(name="金瓶梅",author="生哥",price=56.78)
    # book.save()

    #查询
    # book = Book.objects.get(pk=1)
    # print(book)
    # book = Book.objects.filter(name='西游记').first()
    # print(book)

    # book = Book.objects.get(pk=2)
    # book.delete()

    book = Book.objects.get(pk=1)
    book.price = 200
    book.save()
    return HttpResponse('豆瓣图书')
