from .models import profile
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def profile_pagination(request,profile):
    page = request.GET.get('page')
    num = 4
    paginator = Paginator(profile,num)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page=1
        profiles = paginator.page(page)
    except EmptyPage:
        page =paginator.num_pages
        profiles = paginator.page(page)
    

    leftIndex = int(page) - 4
    if leftIndex < 1 :
        leftIndex = 1
    
    rightIndex = int(page) + 4
 
    if rightIndex > paginator.num_pages :
        rightIndex = paginator.num_pages + 1
    
    custom_range = range(leftIndex,rightIndex)
    
    return profiles,custom_range
    


def search_profile(request):
    search_value = ""
    if request.GET.get('search_value'):
        search_value = request.GET.get('search_value')
    
    profiles=profile.objects.filter(name__icontains=search_value)
    ct = profiles.count()
    print(search_value)

    return profiles,search_value,ct