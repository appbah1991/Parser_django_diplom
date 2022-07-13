from usersapp import views
from django.urls import path
from django.contrib.auth.views import LogoutView
app_name = 'usersapp'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.UserCreateView.as_view(), name='register'),
]