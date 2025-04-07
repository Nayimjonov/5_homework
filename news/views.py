from rest_framework import viewsets
from .models import News
from .serializers import NewsSerializer
from .paginations import NewsPagination


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = NewsPagination
