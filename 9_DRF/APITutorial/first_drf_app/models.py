from django.db import models


# Create your models here.

class Employee(models.Model):
    emp_name =models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    designation = models.CharField(max_length=250)
    salary = models.PositiveIntegerField()



    def __str__(self):
        return self.emp_name