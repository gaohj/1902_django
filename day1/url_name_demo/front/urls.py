from django.urls import path
from . import views
app_name = 'front'

urlpatterns = [
    path('',views.index,name='index'),
    path('denglu/',views.login,name='login')
]