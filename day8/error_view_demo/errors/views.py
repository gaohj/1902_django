from django.shortcuts import render

# Create your views here.
def view_404(request):
    return render(request,'errors/404.html',status=404)

def view_500(request):
    return render(request,'errors/500.html',status=500)