from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def testpage(request):
    return HttpResponse('Heloo Jasil')

def mainpage(request):
    return render(request,'main.html')