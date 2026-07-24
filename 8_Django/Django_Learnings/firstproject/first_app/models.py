from django.db import models
from django.db.models import Q

# Create your models here.

# define database tables



class Department(models.Model):
    department_name = models.CharField(unique=True)

    def __str__(self):
        return self.department_name





class Student(models.Model):                                     # create a table
    name = models.CharField(max_length=250)                      # column name
    age = models.IntegerField()
    address = models.TextField()

    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
