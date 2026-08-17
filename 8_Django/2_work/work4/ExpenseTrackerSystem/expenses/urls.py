from django.urls import path

from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('categories/',views.category_list,name='category_list'),
    path('categories/add/',views.category_create,name='category_create'),
    path('categories/edit/<int:id>/',views.category_update,name='category_update'),
    path('categories/delete/<int:id>/',views.category_delete,name='category_delete'),

    path('expenses/', views.expense_list, name='expense_list'),
    path('expenses/add/', views.expense_create, name='expense_create'),
    path('expenses/edit/<int:id>/', views.expense_update, name='expense_update'),   
    path('expenses/delete/<int:id>/', views.expense_delete, name='expense_delete'),

]


