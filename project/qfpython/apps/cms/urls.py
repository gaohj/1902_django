from django.urls import path
from .import views,course_views,staff_views

app_name = 'cms'
urlpatterns = [
    path('',views.index,name='index'),
    path('write_news/',views.WriteNewsView.as_view(),name='write_news'),
    path('edit_news/',views.EditNewsView.as_view(),name='edit_news'),
    path('news_list/',views.NewsList.as_view(),name='news_list'),
    path('news_category/',views.news_category,name='news_category'),
    path('add_news_category/',views.add_news_category,name='add_news_category'),
    path('upload_file/',views.upload_file,name='upload_file'),
    path('qntoken/',views.qntoken,name='qntoken'),


]

urlpatterns += [
    path('pub_course/',course_views.PublicCourse.as_view(),name='pub_course'),
]

urlpatterns += [
    path('staffs/',staff_views.staff_view,name='staffs'),
    path('add_staff/',staff_views.AddStaffView.as_view(),name='add_staff'),
]