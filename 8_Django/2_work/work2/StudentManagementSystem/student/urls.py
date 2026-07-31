
from django .urls import path
from .import views

urlpatterns = [

    # path('',views.student_list,name='student_list'),
    path('create_student',views.create_student,name='create_student'),
    path('update_student/<int:id>',views.update_student,name='update_student'),
    path('student_details/<int:id>',views.student_details,name='student_details'),
    path('delete_student/<int:id>',views.delete_student,name='delete_student'),
    path('',views.resume,name='resume'),

    path('student_list',views.student_list,name='student_list'),

]
