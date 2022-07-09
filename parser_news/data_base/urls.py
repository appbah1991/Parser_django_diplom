from data_base import views
from django.urls import path

app_name = 'data_base'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('result/', views.result, name='result')
]