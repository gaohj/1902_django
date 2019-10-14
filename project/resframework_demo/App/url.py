# from django.urls import path

from rest_framework import routers

from App import views

router = routers.DefaultRouter()
router.register(r'books',views.BookViewSet)