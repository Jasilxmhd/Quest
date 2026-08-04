from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcomepage'),
    path('register/', views.register, name='registerpage'),
    path('login/', views.user_login, name='loginpage'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),



    path('session/create', views.create_session),
    path('session/get', views.get_session),
    path('session/delete', views.clear_session),
    
    path('cookie/create', views.create_cookie),
    path('cookie/get', views.get_cookie),
    path('cookie/delete', views.delete_cookie),

]