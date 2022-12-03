from django.urls import path
from .views import testview, articleaddview, articleshow, commentaddview, CommentList

urlpatterns = [
    path('', testview),
    path('article-add/', articleaddview),
    path('details/<int:id>', articleshow),
    path('add-comment/', commentaddview),
    path('view-comments/', CommentList.as_view())  #REST API URL
]