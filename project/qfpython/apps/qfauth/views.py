from django.shortcuts import render
from django.contrib.auth import logout,login,authenticate
from django.views.generic import View
from .forms import LoginForm,RegisterForm
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from utils import restful
User = get_user_model()
@require_POST
def register(request):
    form =RegisterForm(request.POST)
    if form.is_valid():
        telephone = form.cleaned_data.get('telephone')
        password = form.cleaned_data.get('password1')
        username = form.cleaned_data.get('username')
        user = User.objects.create_user(telephone=telephone,username=username,password=password)
        login(request,user)
        return restful.success()
    else:
        errors = form.get_errors()
        print(errors)
        return restful.params_error(message=errors)