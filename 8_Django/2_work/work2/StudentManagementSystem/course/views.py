from django.shortcuts import render,redirect
from .models import Course
from .forms import CourseForms
from django.http import HttpResponse





# Create operation
def create_course(request):
    form = CourseForms(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponse("Data Saved Successfully")

    return render(request, "add_course.html", {'form': form})






# Read operation
def list_course(request):
    courses = Course.objects.all()
    return render(request, "listCourse.html", {'courses': courses})





def details(request,id):
    c = Course.objects.get(id =id)
    return render(request,'details.html',{'course':c})






def update_course(request,id):
    data =Course.objects.get(id=id)

    if request.method == 'POST':
        
        f = CourseForms(request.POST,instance=data)

        if f.is_valid():
            f.save()
            return redirect(list_course)
    else:
        f = CourseForms(instance=data)
    return render(request,'update_course.html',{'form':f})



def delete_course(request , id):
    data = Course.objects.get(id = id)

  
    data.delete()
    return redirect(list_course)
