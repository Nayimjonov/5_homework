from rest_framework import serializers
from .models import News
from categories.models import Category
from tags.models import Tag


class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')


class NewsTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'slug')


class NewsSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

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
        read_only_fields = ('slug', 'view_count', 'created_at', 'updated_at', 'is_published')


    def create(self, validated_data):
        tags = validated_data.pop('tags', [])
        instance = News.objects.create(**validated_data)
        instance.tags.set(tags)
        return instance

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] = NewsCategorySerializer(instance.category).data
        rep['tags'] = NewsTagSerializer(instance.tags.all(), many=True).data
        return rep

