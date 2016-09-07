from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=20)
    subject = serializers.CharField(max_length=30)
    text = serializers.CharField(max_length=2000)
    pic = serializers.ImageField()
    date = serializers.DateTimeField()