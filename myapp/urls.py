from django.urls import path
from .views import testview, articleaddview, articleshow, commentaddview

urlpatterns = [
    path('', testview),
    path('article-add/', articleaddview),
    path('details/<int:id>', articleshow),
    path('add-comment/', commentaddview)
]