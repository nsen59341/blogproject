from django.db import models
from django_quill.fields import QuillField

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=124)
    author = models.CharField(max_length=36)
    publication_date = models.DateField()
    # body = models.TextField()
    body = QuillField(blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=36)
    publication_date = models.DateField(null=True)
    body = QuillField(blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
