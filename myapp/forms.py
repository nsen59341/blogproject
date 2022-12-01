from django import  forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # exclude = ['article']
        fields = "__all__"
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'})
        }
