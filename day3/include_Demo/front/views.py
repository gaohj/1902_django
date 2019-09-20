from django.shortcuts import render

def index(request):
    context = {
        'username':'guodongxiong'
    }
    return render(request,'index.html',context=context)

def company(request):
    return render(request,'company.html')

def school(request):
    return render(request,'school.html')