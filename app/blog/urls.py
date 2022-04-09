from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about_us, name='about'),
    path('main/', views.all_articles, name='all_articles'),
    path('contact/', views.feedback, name='contact'),
    path('article/<slug:article_slug>/', views.show_article, name='show_article'),
    path('category/<slug:category_slug>/', views.show_articles_by_category, name='show_cat'),
    path('tag/<slug:tag_slug>/', views.show_articles_by_tag, name='show_tag'),
]
