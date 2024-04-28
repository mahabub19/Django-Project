from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from media.models import post

@api_view(['GET','POST'])
def getRoutes(request):
    routes=[
        {'GET' : '/api/projects/'},
        {'GET' : '/api/projects/id'},
        {'POST' : '/api/projects/id/vote'},
        
        {'POST' : '/api/users/toke/'},
        {'POST' : '/api/users/toke/refresh'},
    ]
    
    return Response(routes)

@api_view(['GET'])
def getPosts(request):
    posts = post.objects.all()
    serializers = PostSerializer(posts, many=True) # Here serializers is a class
    return Response(serializers.data) #add .data to convert it to JASON object

@api_view(['GET'])
def getPost(request,pk):
    posts = post.objects.get(id=pk)
    serializers = PostSerializer(posts, many=False) # Here serializers is a class
    return Response(serializers.data) #add .data to convert it to JASON object