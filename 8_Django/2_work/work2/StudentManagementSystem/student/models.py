from django.db import models
from course.models import Course
from trainer.models import Trainer


# Create your models here.

class Student(models.Model):
    student_name = models.CharField(max_length=250)
    student_email = models.EmailField()
    student_phnno = models.CharField(max_length=15)

    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer,on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name
    