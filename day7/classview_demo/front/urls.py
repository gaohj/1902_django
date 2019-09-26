from django.urls import path
from . import views
from django.views.generic import TemplateView
app_name = 'front'
urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('list/',views.ArticleListView.as_view(),name='list'),
    path('add/',views.add_article,name='add'),
    path('add_article/',views.AddArticleView.as_view(),name='add_article'),
    path('article_detail/<article_id>/',views.ArticleDetail.as_view(),name='article_detail'),
    path('about/',TemplateView.as_view(template_name='about.html')),
]