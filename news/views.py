from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import News
from .serializers import NewsSerializer
from .paginations import NewsPagination
from comments.models import Comment
from comments.serializers import CommentSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = NewsPagination
    lookup_field = 'slug'

    @action(detail=True, methods=['get'], url_path='publish')
    def publish_news(self, request, slug=None):
        try:
            news = self.get_object()
            if news.is_published:
                return Response({'detail': 'Bu yangilik allaqachon eʼlon qilingan.'}, status=status.HTTP_400_BAD_REQUEST)

            news.is_published = True
            news.save()
            return Response({'detail': 'Yangilik muvaffaqiyatli eʼlon qilindi.'}, status=status.HTTP_200_OK)

        except News.DoesNotExist:
            return Response({'detail': 'Yangilik topilmadi.'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['get'], url_path='comments')
    def get_comments(self, request, slug=None):
        news = self.get_object()
        comments = Comment.objects.filter(news=news, is_approved=True).order_by('-created_at')
        page = self.paginate_queryset(comments)
        if page is not None:
            serializer = CommentSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)