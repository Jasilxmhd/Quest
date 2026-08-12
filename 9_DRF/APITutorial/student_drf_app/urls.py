from django.urls import path
from student_drf_app import views

urlpatterns = [

    path('student/', views.get_student, name='student'),

    path('student/create', views.student_create, name='create'),
    path('student/update/<int:id>', views.student_update, name='update'),
    path('student/partial/<int:id>', views.student_partial_update, name='partial'),
    path('student/delete/<int:id>', views.student_delete, name='delete'),
]