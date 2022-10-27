from email.policy import default
from urllib import response
from django.db import models
from django.forms import CharField, IntegerField

# Create your models here.

class Details(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField( default=True)
    # def __str__(self):
    #     return self.name
    
