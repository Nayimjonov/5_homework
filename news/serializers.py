from rest_framework import serializers
from .models import News


class NewsCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    slug = serializers.SlugField(read_only=True)

class NewsTagsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    slug = serializers.SlugField(read_only=True)

class NewsSerializer(serializers.ModelSerializer):
    category = NewsCategorySerializer(read_only=True)
    tags = NewsTagsSerializer(read_only=True, many=True)

    class Meta:
        model = News
        fields = (
            'id',
            'title',
            'slug',
            'content',
            'category',
            'tags',
            'image',
            'view_count',
            'is_published',
            'created_at',
            'updated_at'
        )


