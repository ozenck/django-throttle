from django.urls import path

from .views import ArticleView, AuthorView, ExampleView


app_name = "articles"

urlpatterns = [
    path('articles/', ArticleView.as_view()),
    path('authors/', AuthorView.as_view()),
    path('examples/', ExampleView.as_view())
]