from django.urls import path
from .views import PostCreate, PostList, UpdatePost, DeletePost

urlpatterns = [
    path('create/', PostCreate.as_view(), name='create'),
    path('list/', PostList.as_view(), name='list'),

    path('update/<int:pk>/', UpdatePost.as_view(), name='update'),
    path('delete/<int:pk>/', DeletePost.as_view(), name='delete'),
]