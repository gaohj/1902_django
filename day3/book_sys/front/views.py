from django.shortcuts import render,redirect,reverse
from django.db import connection
# Create your views here.

def get_cursor():
    return connection.cursor()

def index(request):
    cursor = get_cursor()
    cursor.execute("select id,name,author from book")
    books = cursor.fetchall()
    print(books)
    return render(request,'index.html',context={"books":books})

def add_book(request):
    if request.method == 'GET':
        return render(request,'add_book.html')
    else:
        name= request.POST.get('name')
        author=request.POST.get('author')
        cursor = get_cursor()
        cursor.execute("insert into book(id,name,author) values(null,'%s','%s')" % (name,author))
        return redirect(reverse('index'))