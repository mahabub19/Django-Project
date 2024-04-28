from django.urls import path
from . import views

urlpatterns = [
    path("",views.main,name='main'),
    path("posts/",views.posts,name='posts'),
    path("post_details/<str:pk>/",views.post_details,name="post"),
    path("post_form/",views.createForm,name="create_form"),
    path("update_form/<str:pk>/",views.updateForm,name="update_form"),
    path("delete_form/<str:pk>/",views.deleteForm,name="delete_form")
]
