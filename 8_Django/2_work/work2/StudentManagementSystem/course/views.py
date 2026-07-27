from django.shortcuts import render
from .models import Course
from .forms import CourseForms
from django.http import HttpResponse




# Create your views here.

# cred operation

def create_course(request):
    form = CourseForms(request.POST)
    
    if request.method == 'POST':
        
        if form.is_valid():
            form.save()
            return HttpResponse("Data Saved Successfully")


    return render(request,"add_course.html",{'form':form})

    