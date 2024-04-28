from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.logUser,name='login'),
    path("logout/", views.logoutUser,name='logout'),
    path("register/", views.registerUser,name='register'),

    path("account/",views.account,name="account"),
    path("edit-account/",views.edit_account,name="edit-account"),
    path("profiles/", views.profile_f,name='profiles'),
    path("profile/<str:pk>/", views.single_profile,name='profile'),
]
