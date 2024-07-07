from django.db import models

# Create your models here.
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
