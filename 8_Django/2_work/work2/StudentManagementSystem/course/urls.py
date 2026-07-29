
from django.urls import path
from .import views


urlpatterns = [

    path('create_course',views.create_course , name='create_course'),
    path('list_course',views.list_course,name='list_course'),
    path('details/<int:id>',views.details,name='details'),
    path('update/<int:id>', views.update_course, name = 'update'),
    path('delete/<int:id>', views.delete_course, name = 'delete'),
]
