from django.contrib import admin
from .models import Article
# Register your models here.

# admin.site.register(Article)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    list_display_links = ['title', 'author']
    search_fields = ['title']
    list_filter = ['created_date']
    
    class Meta:
        model = Article