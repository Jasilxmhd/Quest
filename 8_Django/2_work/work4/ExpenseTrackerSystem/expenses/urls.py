from django.urls import path

from . import views


urlpatterns = [

    path('categories/',views.category_list,name='category_list'),
    path('categories/add/',views.category_create,name='category_create'),
    path('categories/edit/<int:id>/',views.category_update,name='category_update'),
    path('categories/delete/<int:id>/',views.category_delete,name='category_delete'),

]