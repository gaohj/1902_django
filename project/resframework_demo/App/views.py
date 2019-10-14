from django.shortcuts import render
import uuid
from rest_framework import viewsets,status
from rest_framework.exceptions import APIException,NotFound
from rest_framework.response import Response
from App.models import  Book,Game,Movie,User
from rest_framework.generics import CreateAPIView,ListAPIView,ListCreateAPIView
from App.serializers import (
    BookSerializers,
    Book1Serializers,
    Book2Serializers,
    GameSerializers,
    MovieSerializers,
    UserSerializers,
)
from django.core.cache import cache
from App.authentications import UserAuthentication
from App.permissions import UserPermission

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
    authentication_classes = UserAuthentication
    # permission_classes = UserPermission


# ?action=register
class UserViewSet(CreateAPIView):
    serializer_class = UserSerializers
    def post(self, request, *args, **kwargs):
        action = request.query_params.get('action')
        if action == 'register':
            return self.create(request,*args, **kwargs)
        elif action == 'login':
            return self.do_login(request,*args, **kwargs)
        else:
            raise APIException(detail="请提供正确的操作")

    def do_login(self,request, *args, **kwargs):
        u_name = request.data.get('u_name')
        u_password = request.data.get('u_password')


        try:
            user = User.objects.filter(u_name=u_name).first()
        except User.DoesNotExist as e:
            raise NotFound(detail="该用户不存在")

        if user.u_password != u_password:
            raise APIException(detail="密码错误")

        token = uuid.uuid4().hex

        cache.set(token,user.id,timeout=60*60*24*7)


        data = {
            "status":status.HTTP_200_OK,
            "msg":"登录成功",
            "token":token
        }
        return Response(data)

