from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=36)
    publication_date = models.DateField()
    body = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=36)
    publication_date = models.DateField()
    body = models.TextField()


