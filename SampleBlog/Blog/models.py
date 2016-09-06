from django.db import models

class BlogPost(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    title = models.CharField(max_length=25)
    subject = models.CharField(max_length=30, choices=[('P', 'Personal'), ('W', 'Work')])
    text = models.TextField(null=False)
    pic = models.ImageField(upload_to='static/img/', default='static/img/no-image.png')
    date = models.DateTimeField()

    def __str__(self):
        return self.title

