from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def welcome(request):
    return render(request,'welcome.html')

def mainpage(request):
    return render(request,'main.html')

def aboutpage(request):
    return render(request,'about.html')

def loginpage(request):
    return render(request,'login.html')