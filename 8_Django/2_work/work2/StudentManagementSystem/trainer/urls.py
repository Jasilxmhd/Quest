
from django.urls import path
from .import views

urlpatterns = [

    path('add',views.create_trainer,name='add'),
    
    # path('trainer_list',views.trainer_list,name='trainer_list'),
    path('list',views.trainer_list,name='trainer_list'),
    path('details/<int:id>',views.details,name='trainer_details'),
    path('update/<int:id>', views.update_trainer, name = 'update_trainer'),
    path('delete/<int:id>', views.delete_trainer, name = 'delete_trainer'),

]
