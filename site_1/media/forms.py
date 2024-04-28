from django.forms import ModelForm
from .models import post
from django import forms

class postForm(ModelForm):
    class Meta:
        model = post
        fields = ['user','title','post_type','description','feature_image','reference_link']
        widgets ={
            'post_type' : forms.CheckboxSelectMultiple()
        }

    def __init__(self,*args,**kwargs):
        super(postForm,self).__init__(*args,**kwargs)

        # for name,field in self.fields.items():
        #     field.widget.attrs.update({'class':'form-control'})
        self.fields['title'].widget.attrs.update({'class':'form-control'})
        self.fields['description'].widget.attrs.update({'class':'form-control'})
        self.fields['feature_image'].widget.attrs.update({'class':'form-control'})
        self.fields['reference_link'].widget.attrs.update({'class':'form-control'})
