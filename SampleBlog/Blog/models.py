from django.db import models
from django.utils import timezone

# Create your models here.
class BlogPost(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    subject = models.CharField(max_length=100, null=False)
    text = models.TextField(null=False)
    pic = models.ImageField(upload_to='static/img/', default='static/img/no-image.png')
    date = models.DateTimeField()

    def __str__(self):
        return self.subject