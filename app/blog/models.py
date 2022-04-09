from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_abs_url_category(self):
        return reverse('show_cat', kwargs={'category_slug': self.slug})


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_abs_url_tag(self):
        return reverse('show_tag', kwargs={'tag_slug': self.slug})


class Article(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    tag = models.ManyToManyField('Tag')
    is_published = models.BooleanField(default=True)
    creation_date = models.DateField(auto_now_add=True)
    date_of_change = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    photo = models.FileField(upload_to='photos/%Y/%m/%d/')

    class Meta:
        ordering = ['creation_date']

    def __str__(self):
        return self.title

    def get_abs_url_article(self):
        return reverse('show_article', kwargs={'article_slug': self.slug})


class Message(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return f'Subject: {self.subject}'


class Comment(models.Model):
    article = models.ForeignKey('Article',on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.article}"
