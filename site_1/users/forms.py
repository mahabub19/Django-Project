from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import profile

class account_form(ModelForm):
    class Meta:
        model = profile
        fields =['username','name','email','bio','profile_image']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','email','password1','password2']
        labels ={
            'username' : 'Name'
        }

    def __init__(self,*args,**kwargs):
        super(CustomUserCreationForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':'xyz'})
        self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':'xyx@gmail.com'})
        self.fields['password1'].widget.attrs.update({'class':'form-control','placeholder':'xYz6183%#'})
        self.fields['password2'].widget.attrs.update({'class':'form-control','placeholder':'same as before'})