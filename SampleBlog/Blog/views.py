from django.shortcuts import render
from . import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BlogPost, Subject


@api_view(['GET'])
def getBlogPosts(request, category):
    posts = BlogPost.objects.filter(subject__subject=category)
    serializer = serializers.BlogPostSerializer(posts, many=True)
    return Response(serializer.data)

def homepage(request):
    Choices = [x for x in Subject.objects.all()]
    return render(request, "homepage.html", {'subjects':Choices})


def blogPage(request):
    return render(request, 'blogpage.html')