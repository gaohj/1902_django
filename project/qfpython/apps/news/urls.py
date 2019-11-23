from django.urls import path

from . import views
app_name = 'news'

urlpatterns = [
    path('list/',views.news_list,name='news_list'),
]