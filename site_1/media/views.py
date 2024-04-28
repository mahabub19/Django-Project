from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import post,review
from .forms import postForm
from django.contrib.auth.decorators import login_required
from .utils import search_post,post_pagination
# Create your views here.

def main(request):
    return render(request,'media_main.html')
    
@login_required(login_url='login')
def posts(request):

    posts , search_value,count = search_post(request)
    custom_range, posts = post_pagination(request,posts)
    context = {'posts':posts,'custom_range':custom_range,
    'count':count,'search_value': search_value}
    return render(request,'media/posts.html',context)

@login_required(login_url='login')
def post_details(request,pk):
    profile = request.user.profile
    data=post.objects.get(id=pk)
    post_type = data.post_type.all()
    reviews = data.review_set.all()
    context = {'profile':profile,'record':data,'type':post_type,'reviews':reviews,'id':pk}
    return render(request,'media/posts_details.html',context)

@login_required(login_url='login')
def createForm(request):
    form = postForm()
    if request.method=='POST':
        data = postForm(request.POST, request.FILES)
        if data.is_valid():
            form = data.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('posts')
    context ={'form': form}
    return render(request,'media/post_form.html',context)

@login_required(login_url='login')
def updateForm(request,pk):
    p = post.objects.get(id=pk)
    form = postForm(instance=p)
    if request.method=='POST':
        data = postForm(request.POST,request.FILES,instance=p)
        if data.is_valid():
            data.save()
            return redirect('posts')
    context ={'form': form}
    return render(request,'media/post_form.html',context)

@login_required(login_url='login')
def deleteForm(request,pk):
    p = post.objects.get(id=pk)
    if request.method=='POST':
        p.delete()
        return redirect('posts')
    context ={'post': p}
    return render(request,'media/delete.html',context)
    

