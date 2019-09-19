from django.shortcuts import render
from datetime import datetime
def greet(word):
    return "hello world %s" % word

def index(request):
    context = {
        'greet':greet
    }
    return render(request,'index.html',context=context)

def add_view(request):
    context = {
        'value1': ['1','2','3','4'],
        'value2':[5,'6',7]
    }
    return render(request, 'add.html', context=context)

def cut_view(request):
    return render(request, 'cut.html')

def date_view(request):
    context = {
        'today':datetime.now()
    }
    return render(request, 'date.html',context=context)

def default_view(request):
    context = {
        'value':'haha'
    }
    return render(request, 'default.html',context=context)