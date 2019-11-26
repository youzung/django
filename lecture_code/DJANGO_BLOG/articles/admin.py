from django.contrib import admin
from .models import Article
from .models import Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'image', 'created_at', 'updated_at')

admin.site.register(Article, ArticleAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'created_at', 'article_id')

admin.site.register(Comment, CommentAdmin)