from django.shortcuts import render
from django.http import HttpResponse
from .models import News,NewsCategory
# Create your views here.
def index(request):
    newses = News.objects.all()
    categories = NewsCategory.objects.all()
    context = {
        'newses':newses,
        'categories':categories,
    }
    return render(request,'news/index.html',context=context)

def list(request):
    return HttpResponse("list")