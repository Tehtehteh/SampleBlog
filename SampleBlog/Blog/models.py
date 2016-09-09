from django.db import models

class Subject(models.Model):
    subject = models.CharField(max_length=20)

    def __str__(self):
        return self.subject[0].upper() + self.subject[1:].lower()

class BlogPost(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    title = models.CharField(max_length=25)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    text = models.TextField(null=False)
    pic = models.ImageField(upload_to='static/img/', default='static/img/no-image.png')
    date = models.DateTimeField()

    def __str__(self):
        return self.title

