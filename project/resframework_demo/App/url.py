# from django.urls import path
from django.conf.urls import url
from rest_framework import routers

from App import views

router = routers.DefaultRouter()
router.register(r'books',views.BookViewSet)


urlpatterns = [
    # path('game/',views.GameViewSet.as_view(),name='game'),
    url(r'^game/',views.GameViewSet.as_view(),name='game'),
    url(r'^movies/$',views.MovieViewSet.as_view(
        actions={
            "get":"list",
            "post":"create",
        }
    ),name='movie'),#上面只能是增加或者查看所有 不能根据id查看某一个
    url(r'^movies/(?P<pk>\d+)/', views.MovieViewSet.as_view(
        actions={
            "get": "retrieve",
            "put": "update",
            "patch":"partial_update",
            "delete":"destroy",
        }
    ), name='movies'),#这个实现根据id查看某一个 或者更新 或者删除
    url(r'^users/',views.UserViewSet.as_view(),name="users")
]

#418794186d364c7f8401a5da9f2e0985