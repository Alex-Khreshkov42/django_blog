from django.core.mail import BadHeaderError, send_mail
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.urls import reverse
from .models import *

from .forms import ContactForm, CommentForm
from .models import Author, Category, Tag, Article


def all_articles(request):
    articles_for_slider = get_list_or_404(Article)
    articles = Article.objects.filter(is_published=True).order_by('-id')
    if request.method == 'GET':
        search_article = request.GET.get('q')
        if search_article:
            articles = Article.objects.filter(is_published=True, title__contains = search_article).order_by('-id')

    tags = get_list_or_404(Tag)
    paginator = Paginator(articles, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = get_list_or_404(Category)
    context = {
        'title': 'Main',
        'articles': articles,
        'tags': tags,
        'categories': categories,
        'page_obj': page_obj,
        'articles_for_slider':articles_for_slider,
    }
    return render(request, 'blog/blog.html', context=context)


def show_article(request, article_slug):
    article = get_object_or_404(Article, slug=article_slug)
    articles = get_list_or_404(Article)[:5]
    tags = get_list_or_404(Tag)
    categories = get_list_or_404(Category)
    comments = Comment.objects.filter(article=article)
    comments_count = comments.count()
    print(comments.count())
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.article = article
            form.save()
            return redirect(article.get_abs_url_article())
    else:
        comment_form = CommentForm()

    context = {
        'title': article.title,
        'article_title': article.title,
        'tags': tags,
        'categories': categories,
        'articles': articles,
        'article': article,
        'comments': comments,
        'comments_count': comments_count,
        'form': comment_form,
    }
    return render(request, 'blog/post-details.html', context=context)


def show_articles_by_category(request, category_slug):
    articles = get_list_or_404(Article, category__slug=category_slug)
    tags = get_list_or_404(Tag)
    paginator = Paginator(articles, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = get_list_or_404(Category)
    context = {
        'title': 'Main',
        'articles': articles,
        'tags': tags,
        'categories': categories,
        'page_obj': page_obj,
    }
    return render(request, 'blog/show_article_by_category.html', context=context)


def show_articles_by_tag(request, tag_slug):
    articles = get_list_or_404(Article, tag__slug=tag_slug)
    categories = get_list_or_404(Category)
    tags = get_list_or_404(Tag)
    paginator = Paginator(articles, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': 'Main',
        'articles': articles,
        'tags': tags,
        'categories': categories,
        'page_obj': page_obj,
    }
    return render(request, 'blog/show_by_tag.html', context=context)


def about_us(request, ):
    context = {
        'title': 'About Us',
    }
    return render(request, 'blog/about.html', context=context)


def feedback(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            Message.objects.create(**form.cleaned_data)
            return redirect('contact')
    else:
        form = ContactForm()

    context = {
        'title': 'Contact Us',
        'form': form,
    }
    return render(request, 'blog/contact.html', context=context)
