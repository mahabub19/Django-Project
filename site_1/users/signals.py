from django.contrib.auth.models import User
from django.db.models.signals import post_save,post_delete
from .models import profile

from django.conf import settings
from django.core.mail import send_mail

def profileUpdated(sender,instance,created,**kwargs):
    if created :
        user = instance
        profile.objects.create(
            user=instance,
            username=user.username,
            email=user.email,
            name=user.username
        )

        subject = 'CSE Club of JUST'
        message = 'Well to our useless Culb of Jashore University of Science and Technology'
        mail_form = settings.EMAIL_HOST_USER
        mail_to = [user.email]

        send_mail(subject,message,mail_form,mail_to,fail_silently=False,)
        

    
def userUpdated(sender,instance,created,**kwargs):
    profile = instance
    user  = profile.user 
    if created==False :
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()
    


def profileDeleted(sender,instance,**kwargs):
    user = instance.user
    user.delete()
    

post_save.connect(profileUpdated,sender=User)
post_save.connect(userUpdated,sender=profile)
post_delete.connect(profileDeleted,sender=profile)