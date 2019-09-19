from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('list/',views.list,name='list')
]