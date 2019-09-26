from django.urls import path
from . import views

app_name = 'front'
urlpatterns = [
    path('add/',views.add_article,name='add'),
    path('add_article/',views.AddArticleView.as_view(),name='add_article'),
    path('article_detail/<article_id>/',views.ArticleDetail.as_view(),name='article_detail')
]