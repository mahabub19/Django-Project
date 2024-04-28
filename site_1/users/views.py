from django.shortcuts import redirect, render
from .models import profile
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
# from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
from .forms import account_form
from .utils import profile_pagination, search_profile

# Create your views here.

def logUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('main')
    
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
    
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,"Invalid username")
        
        user = authenticate(request,username=username,password=password) # search for user in database
        
        if user is not None:
            login(request , user)#create a session in browser for user.
            return render(request, 'media_main.html')
        else:
            messages.error(request,"Incorrect Username or password")

    
    return render(request,'users/log_reg_page.html',{'page':page})

def logoutUser(request):
    logout(request)
    messages.error(request,"Successfully logged out") 
    return redirect('login')


def registerUser(request):
    page='register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            messages.success(request,'Successful registration')
            login(request,user)
            return redirect('edit-account')
        else:
            messages.success(request,'Registration failed')


    context={'page':page,'form':form}
    return render(request,'users/log_reg_page.html',context)

@login_required(login_url='login')
def profile_f(request):
    profiles, search_value,count = search_profile(request)
    profiles,custom_range = profile_pagination(request,profiles)

    context ={'profiles':profiles,'custom_range':custom_range,'count':count,'search_value': search_value}
    return render(request,'users/profiles.html',context) 

@login_required(login_url='login')
def single_profile(request,pk):
    ob = profile.objects.get(id=pk)
    context={'profile':ob}
    return render(request,'users/profile.html',context) 


@login_required(login_url='login')
def account(request):
    profile = request.user.profile
    skill = request.user.profile.skill_set.all()
    posts = request.user.post_set.all()
    context={'profile':profile,'skill':skill,'posts':posts }
    return render(request,'users/account.html',context)

def edit_account(request):
    profile = request.user.profile
    form = account_form(instance=profile)
    context={'form':form}
    if request.method == 'POST':
        form = account_form(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')

    return render(request,'users/edit-account.html',context)
