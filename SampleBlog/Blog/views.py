from django.shortcuts import render
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BlogPost


@api_view(['GET'])
def getBlogPosts(request):
    posts = BlogPost.objects.all()
    serializer = serializers.BlogPostSerializer(posts, many=True)
    return Response(serializer.data)

def homepage(request):
    Choices = [x[1] for x in BlogPost._meta.get_field('subject').choices]
    post = BlogPost.objects.all()
    return render(request, "homepage.html", {'subjects':Choices, 'post':post})


def blogPage(request):
    return render(request, 'blogpage.html')