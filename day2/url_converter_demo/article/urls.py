from django.urls import re_path,path
from . import views
urlpatterns = [
    path('',views.article),
    #\w 0-9 a-z A-Z _
    # a|b
    re_path(r'list/(?P<categories>\w+|(\w+\+\w+)+)/',views.article_list),
]

