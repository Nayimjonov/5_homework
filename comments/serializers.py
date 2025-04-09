from rest_framework import serializers
from .models import Comment
from news.models import News


class NewsCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'slug')

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

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['news'] = NewsCommentSerializer(instance.news).data
        return rep