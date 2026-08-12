from django.db import models


# Create your models here.

class Student(models.Model):
    stud_name =models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=100)
    age = models.IntegerField()
    place = models.TextField(blank=True)



    def __str__(self):
        return self.stud_name

