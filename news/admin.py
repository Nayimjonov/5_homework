from django.contrib import admin
from django.utils.html import mark_safe

from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'view_count',
        'is_published'
    )
    search_fields = ('title', 'content', 'slug')
    list_filter = ('category', 'tags', 'is_published')
    prepopulated_fields = {'slug': ('title',)}


