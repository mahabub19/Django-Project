from django.contrib import admin
from .models import post,review,type

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display=('title','description','feature_image','reference_link')
class ReviewAdmin(admin.ModelAdmin):
    list_display=('post','feedback','value','created')
class TypeAdmin(admin.ModelAdmin):
    list_display=('name','created')

# admin.site.register(post,PostAdmin,ReviewAdmin,TypeAdmin,review,type)
admin.site.register(post,PostAdmin)
admin.site.register(review,ReviewAdmin)
admin.site.register(type,TypeAdmin)