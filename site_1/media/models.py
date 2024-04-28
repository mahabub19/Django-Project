import uuid
from django.db import models
from django.contrib.auth.models import User

class type(models.Model):
    name = models.CharField(max_length=200,blank=True)
    created = models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.name

class post(models.Model):
    user = models.ForeignKey(User,null=True,blank=True , on_delete=models.CASCADE)
    title = models.CharField(max_length=200,blank=True)
    post_type = models.ManyToManyField(type,blank=True,null=True)
    description =models.TextField(max_length=400,blank=True)
    feature_image= models.ImageField(null=True,blank=True,default="default.png")
    reference_link= models.CharField(max_length=200,blank=True)
    created = models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
    
class review(models.Model):
    vote=(
        ('like','like'),
        ('dislike','dislike'),
        ('love','love'),
        ('celebrate','celebrate'),
        ('sad','sad'),
    )
    user = models.ForeignKey(User,null=True,blank=True , on_delete=models.CASCADE)
    post = models.ForeignKey(post,on_delete=models.CASCADE,blank=True)
    feedback = models.CharField(max_length=200,blank=True)
    value= models.CharField(max_length=100,choices=vote,blank=True)
    created = models.DateTimeField(auto_now_add=True,blank=True)
    # def __str__(self):
    #     return self.post
    



