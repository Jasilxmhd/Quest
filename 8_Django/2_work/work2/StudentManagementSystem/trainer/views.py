from django.shortcuts import render,redirect
from .models import Trainer
from .forms import Trainerform

from django.http import HttpResponse

# Create your views here.

def create_trainer(request):

    if request.method == 'POST':
        f = Trainerform(request.POST)
        if f.is_valid():
            f.save()

            return HttpResponse("Form saved Successfully")

    else:
        f = Trainerform()
    return render(request,'trainer/add_trainer.html',{'form':f})






def trainer_list(request):
    trainer = Trainer.objects.all()
    return render(request, "trainer/trainer_list.html", {'trainer': trainer})





def details(request,id):
    t = Trainer.objects.get(id =id)
    return render(request,'trainer/trainer_details.html',{'trainer':t})






def update_trainer(request,id):
    data =Trainer.objects.get(id=id)

    if request.method == 'POST':
        
        f = Trainerform(request.POST,instance=data)

        if f.is_valid():
            f.save()
            return redirect(trainer_list)
    else:
        f = Trainerform(instance=data)
    return render(request,'trainer/update_trainer.html',{'form':f})



def delete_trainer(request , id):
    data = Trainer.objects.get(id = id)

  
    data.delete()
    return redirect(trainer_list)
