from django.urls import path
from . import views


app_name = 'qfauth'

urlpatterns = [
    path('register/',views.register,name='register'),
]