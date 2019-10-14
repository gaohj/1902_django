from django.shortcuts import render
from rest_framework import viewsets
from App.models import  Book,Game,Movie
from rest_framework.generics import CreateAPIView,ListAPIView,ListCreateAPIView
from App.serializers import (
    BookSerializers,
    Book1Serializers,
    Book2Serializers,
    GameSerializers,
    MovieSerializers
)

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    # serializer_class = BookSerializers
    serializer_class = Book2Serializers

#这个方法只能用来新增数据 也就是仅仅允许 post方法
# class GameViewSet(CreateAPIView):
#     queryset = Game.objects.all()
#     serializer_class = GameSerializers
#

#这个CBV类视图 仅仅用来查看 只允许get方法
# class GameViewSet(ListAPIView):
#     queryset = Game.objects.all()
#     serializer_class = GameSerializers

#只能 get请求 和 post请求 其它都不允许
class GameViewSet(ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializers


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers

