from data_base import views
from django.urls import path, include, re_path


app_name = 'data_base'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('result_bv/', views.NewsListView.as_view(), name='result_bv'),
    path('news_delete_confirm/<int:pk>', views.NewsDeleteView.as_view(), name='news_delete'),
]