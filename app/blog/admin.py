from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject', 'email','message')
    list_display_links = ('name', 'email')
    search_fields = ('email',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'name', 'email', 'content', 'active')
    list_display_links = ('article', 'email', 'active')
    search_fields = ('article', 'name', 'email')


class ArticeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'author', 'creation_date', 'get_html_photo', 'is_published')
    list_display_links = ('title',)
    list_editable = ('is_published',)
    list_filter = ('creation_date', 'is_published')
    search_fields = ('title', 'category')
    prepopulated_fields = {"slug": ("title",)}

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width = 80>")

    get_html_photo.short_description = 'photo'


admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticeAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Message, MessageAdmin)
