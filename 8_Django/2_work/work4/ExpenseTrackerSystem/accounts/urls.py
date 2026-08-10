from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.dashboard, name='dashboard'),

    path('register/', views.register, name='registerpage'),
    path('login/', views.user_login, name='loginpage'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),


]