from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .forms import ArticleForm, CommentForm
from .models import Article, Comment

# Create your views here.

def testview(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles':articles})

def articleaddview(request):
    if request.method == 'GET':
        article_form = ArticleForm()
        return render(request, 'addarticle.html', {'article_form': article_form})
    else:
        data = request.POST
        # print(data)
        article = Article()
        article.title = data['title']
        article.author = data['author']
        article.body = data['body']
        article.publication_date = data['publication_date']
        article.save()
        return HttpResponseRedirect('/myapp')

def articleshow(request, id=1):
    comment_form = CommentForm()
    article = Article.objects.get(id=id)
    comments = Comment.objects.filter(article=id)

    return render(request, 'show_detals.html', {'article': article, 'comments': comments , 'comment_form': comment_form})


def commentaddview(request):
    data = request.POST
    # print(data)
    comment = Comment()
    comment.article = data['article']
    comment.title = data['title']
    comment.author = data['author']
    comment.body = data['body']
    comment.publication_date = data['publication_date']
    comment.save()
    return HttpResponseRedirect('')