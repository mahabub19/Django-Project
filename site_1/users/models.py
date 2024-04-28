from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete



# Create your models here.


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True)
    name= models.CharField(max_length=100,blank=True,null=True)
    username = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    bio= models.CharField(max_length=300,blank=True,null=True)
    profile_image= models.ImageField(blank=True,null=True,upload_to='profile/',default='default.png')
    def __str__(self):
        return self.name

class skill(models.Model):
    user = models.ForeignKey(profile,blank=True,null= True,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True,blank=True)
    description = models.CharField(max_length=500,null=True,blank=True)
    def __str__(self):
        return self.name
    


    
    
    
    