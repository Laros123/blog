from django.db import models

# Create your models here.


class Post(models.Model):
    name = models.CharField(max_length=127)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)


class Commentary(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=1)
    text = models.TextField()
    author = models.IntegerField()
    date = models.DateTimeField(auto_now=True)



