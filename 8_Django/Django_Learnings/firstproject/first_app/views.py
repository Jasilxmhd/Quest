from django.shortcuts import render
from django.http import HttpResponse
from .models import Department,Student

# Create your views here.


def home(request):                                              # request is madatory
    return HttpResponse("Hello... Welcome to Home Page...")

def about(request):
    return HttpResponse("This is about page .")

def homes(request):
    return render(request,'home.html')



def view_student(request):
    stud = Student.objects.all()
    name = 'jasil muhammed'
    return render(request,'student.html',{'student' : stud, 'sname':name})