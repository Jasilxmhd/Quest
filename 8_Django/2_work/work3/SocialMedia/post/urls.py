from django.urls import path
from .import views
from .views import PostCreate, PostList, UpdatePost, DeletePost

urlpatterns = [
    path('create/', PostCreate.as_view(), name='create'),
    path('list/', PostList.as_view(), name='list'),
    path('update/<int:pk>/', UpdatePost.as_view(), name='update'),
    path('delete/<int:pk>/', DeletePost.as_view(), name='delete'),

    path('post/create/',views.post_create,name="post_create"),
    path('post/list/',views.post_list,name="post_list"),
    path('post/update/<int:id>/', views.post_update, name="post_update"),
    path('post/delete/<int:id>/', views.post_delete, name="post_delete"),

    path('send/',views.send_html_email,name ='name'),

]