from django.urls import re_path
from . import views

urlpatterns = [
    # r''代表原生字符串  raw
    re_path(r'^$',views.article),
    re_path(r'^list/(?P<year>(1[3-9]\d{9}))/$',views.article_list),
    re_path(r'^list/(?P<month>\d{2})/$',views.article_list_month),
]