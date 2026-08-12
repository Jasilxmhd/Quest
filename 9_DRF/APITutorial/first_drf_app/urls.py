from django.urls import path
from first_drf_app import views

urlpatterns = [
    # path('greet/', views.greet, name='greet'),
    path('employee/', views.get_employee, name='employee'),

    path('employee/create', views.employee_create, name='create'),
    path('employee/update/<int:id>', views.employee_update, name='update'),
    path('employee/partial/<int:id>', views.employee_partialupdate, name='partial'),

    path('employee/delete/<int:id>', views.employee_delete, name='delete'),
]