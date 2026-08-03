from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcomepage'),
    path('register/', views.register, name='registerpage'),
    path('login/', views.user_login, name='loginpage'),
    path('home/', views.home, name='home'),
]