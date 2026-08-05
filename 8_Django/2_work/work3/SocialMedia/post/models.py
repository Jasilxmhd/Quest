from django.db import models
from django.urls import reverse

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=250) 
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='post/')

    def __str__(self):
        return self.title

    def get_absolute_url(self): 
        return reverse('list')


    