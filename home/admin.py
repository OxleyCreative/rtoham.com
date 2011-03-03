from home.models import Article
from django.contrib import admin

class ArticleAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'show_on_homepage', 'order']

admin.site.register(Article, ArticleAdmin)
