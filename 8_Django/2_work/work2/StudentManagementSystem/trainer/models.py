from django.db import models
from course.models import Course

# Create your models here.

class Trainer(models.Model):
    trainer_name = models.CharField(max_length=250)
    trainer_email = models.EmailField()

    course = models.ForeignKey(Course, on_delete=models.CASCADE)           # CASCADE used to block a perent delete option

    def __str__(self):
        return self.trainer_name

    