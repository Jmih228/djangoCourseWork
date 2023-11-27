from django.contrib import admin
from blog.models import Blog_Post


@admin.register(Blog_Post)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'views_count', 'publication_date')
    list_filter = ('title', 'views_count', 'publication_date')
    search_fields = ('title', 'content', 'publication_date')
