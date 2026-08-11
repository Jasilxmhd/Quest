from django.urls import path
from first_drf_app import views

urlpatterns = [
    path('greet/', views.greet, name='greet'),
]