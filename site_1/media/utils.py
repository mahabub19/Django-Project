from .models import post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def post_pagination(request,posts):
    page = request.GET.get('page')
    num = 4
    paginator = Paginator(posts,num)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        page=1
        posts = paginator.page(page)
    except EmptyPage:
        page =paginator.num_pages
        posts = paginator.page(page)
    

    leftIndex = int(page) - 4
    if leftIndex < 1 :
        leftIndex = 1
    
    rightIndex = int(page) + 4
 
    if rightIndex > paginator.num_pages :
        rightIndex = paginator.num_pages + 1
    
    custom_range = range(leftIndex,rightIndex)
    
    return custom_range,posts
    


def search_post(request):
    search_value = ""
    if request.GET.get('search_value'):
        search_value = request.GET.get('search_value')
    
    posts=post.objects.filter(title__icontains=search_value)
    count = posts.count()

    return posts,search_value,count