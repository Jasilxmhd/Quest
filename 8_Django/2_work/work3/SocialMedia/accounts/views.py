from django.shortcuts import render,redirect
from .forms import CustomUserForm,LoginForm
from django.http import HttpResponse
from  django.contrib.auth import login,logout,authenticate
# Create your views here.

def register(request):
    form =CustomUserForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            form.save()
            return HttpResponse('User Registered Successfully')
        else:
            return HttpResponse('Invalid Form')
    else:
        form = CustomUserForm()
    return render(request,'register.html',{'form':form})


def home(request):
    return HttpResponse("This is Home Page.....")



def user_login(request):
    if request.method == 'POST':
        login_form=LoginForm(request.POST)
        
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            
            user =authenticate(request,username=username,password=password)
            
            if user is not None:
                login(request,user)
                return redirect('home')          
            else:
                return HttpResponse("Invalid USer")
    else:
        login_form=LoginForm()
    return render(request,'login.html',{'login_form':login_form})






def welcome(request):
    return render(request, 'welcome.html')