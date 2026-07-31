
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .import settings

from course import views

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('course/',include('course.urls')),                                # course is a app name 

    path('',include('trainer.urls')),

    path('list_course/',views.list_course, name='list_course'),
    path('',include('student.urls')),
                           

]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
    )