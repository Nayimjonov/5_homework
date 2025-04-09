from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'news',
            'author_name',
            'author_email',
            'content',
            'is_approved',
            'created_at',
        )