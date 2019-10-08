from django.shortcuts import render,redirect,reverse
from .models import User
from .forms import SignUpForm,SignInForm
from django.views.generic import View
from django.contrib import messages
# Create your views here.

def index(request):
    users = User.objects.all()
    for user in users:
        print(user.username)
    return render(request,'index.html',context={"username":user.username})

class SignUpView(View):
    def get(self,request):
        return render(request,'register.html')

    def post(self,request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            # username = form.cleaned_data.get('username')
            # telephone = form.cleaned_data.get('telephone')
            # print(username,telephone)
            form.save()
            return redirect(reverse('index'))
        else:
            #{"telephone":[""]}
            print(form.errors.get_json_data())
            return redirect(reverse('signup'))


class SignInView(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.filter(username=username,password=password).first()
            if user:
                request.session['user_id'] = user.id
                return redirect(reverse('index'))
            else:
                messages.info(request,'用户名或者密码错误')
                return redirect(reverse('signin'))
        else:
            errors = form.get_errors()
            for error in  errors:
                messages.info(request,error)
            return redirect(reverse('signin'))

def log_out(request):
    request.session.flush()
    return redirect(reverse('index'))