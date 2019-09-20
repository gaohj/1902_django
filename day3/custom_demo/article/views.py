from django.shortcuts import render
from datetime import datetime
# Create your views here.
def index(request):
    context = {
       'value':'guodong',
        'mytime':datetime(year=2019,month=9,day=19,hour=10,minute=7,second=30)
    }
    return render(request,'index.html',context=context)
