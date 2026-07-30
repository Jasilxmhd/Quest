from django.shortcuts import render,redirect
from .models import Student
from .forms import Studentform

from django.http import HttpResponse

# Create your views here.


def create_student(request):

    if request.method == 'POST':
        f = Studentform(request.POST)
        if f.is_valid():
            f.save()

            return HttpResponse("Form saved successfully")

    else:
        f = Studentform()
    return render(request,'student/add_student.html',{'form':f})




def student_list(request):
    student = Student.objects.all()
    return render(request,'student/student_list.html',{'student':student})

    


def student_details(request,id):
    j = Student.objects.all()
    return render(request,'student/student_details.html',{'student':j})



def update_student(request,id):
    data =Student.objects.get(id=id)

    if request.method == 'POST':
        
        f = Studentform(request.POST,instance=data)

        if f.is_valid():
            f.save()
            return redirect(student_list)
    else:
        f = Studentform(instance=data)
    return render(request,'update_trainer.html',{'form':f})






def delete_student(request , id):
    data = Student.objects.get(id = id)

  
    data.delete()
    return redirect(student_list)