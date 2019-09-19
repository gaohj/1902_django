from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render
# Create your views here.
def index(request):
    # # return HttpResponse("ADSFADS")
    # html = render_to_string('index.html')
    # return HttpResponse(html)
    return render(request,'index.html')