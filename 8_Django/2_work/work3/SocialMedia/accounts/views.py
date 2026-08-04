from django.shortcuts import render,redirect
from .forms import CustomUserForm,LoginForm
from django.http import HttpResponse
from  django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.





def welcome(request):
    return render(request, 'welcome.html')







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


@login_required(login_url='login')
def home(request):
    return render(request,'home.html')



def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        login_form=LoginForm(request.POST)
        
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            
            user = authenticate(request,username=username,password=password)
            
            if user is not None:
                request.session['username'] = username
                login(request,user)
                return redirect('home')          
            else:
                return HttpResponse("Invalid USer")
    else:
        login_form=LoginForm()
    u = request.session.get('username')
    return render(request,'login.html',{'login_form':login_form , 'user':u })








def logout_view(request):
    logout(request)
    return redirect(user_login)







# Session



def create_session(request):
    request.session['username'] = 'john'                              # username is key
    request.session['email'] = 'john@example.com'
    return HttpResponse("Session Created")




def get_session(request):
    u_name = request.session.get('username')
    return HttpResponse(u_name)




def clear_session(request):
    request.session.flush()                                            # remove full data
    return HttpResponse('All session data removed')



# cookie


def create_cookie(request):
    response = HttpResponse("cookie created")
    response.set_cookie('username', 'john' , max_age=3600)  # 1 hour
    return response

def get_cookie(request):
    username = request.COOKIES.get('username')
    return HttpResponse(username or 'NO cookie found')

def delete_cookie(request):
    response =HttpResponse("cookie deleted")
    response.delete_cookie("username")
    return response