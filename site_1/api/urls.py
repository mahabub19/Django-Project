from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes,name='api'),
    path('posts/',views.getPosts,name='api_posts'),
    path('posts/<str:pk>/',views.getPost,name='api_post'),
]

