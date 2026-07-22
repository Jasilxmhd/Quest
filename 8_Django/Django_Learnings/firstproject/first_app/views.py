from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):                                                   # request is madatory
    return HttpResponse("Hello... Welcome to Home Page...")

def about(request):
    return HttpResponse("This is about page .")

def homes(request):
    return render(request,'home.html')