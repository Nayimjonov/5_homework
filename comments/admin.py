from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_name', 'author_email', 'is_approved')
    search_fields = ('is_approved', 'author_email')
    list_filter = ('news', 'is_approved')

