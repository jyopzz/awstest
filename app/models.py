import datetime
import os
from django.db import models


# Create your models here.

class Getnamemod(models.Model):
    name=models.CharField(max_length=250)
    image= models.ImageField(upload_to="images/",null=True,blank=True)
    def __str__(self):

        return self.name 
    
class details(models.Model):
    name=models.CharField(max_length=200,)
    image=models.ImageField(upload_to='images/',null=True,blank=True)
    def __str__(self):
        return self.name