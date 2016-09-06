from django.shortcuts import render
from . import serializers
from .models import Subject

def homepage(request):
    Choices = [x[1] for x in Subject._meta.get_field('subject').choices]
    return render(request, "homepage.html", {'subjects':Choices})


def blogPage(request):
    return render(request, 'blogpage.html')