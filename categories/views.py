from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer
from .pagination import CategoryPagination


class CategoryViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Category.objects.all()
        paginator = CategoryPagination()
        page = paginator.paginate_queryset(queryset, request)
        serializer = CategorySerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        category = get_object_or_404(Category, slug=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def update(self, request, pk=None):
        category = get_object_or_404(Category, slug=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        category = get_object_or_404(Category, slug=pk)
        category.delete()
        return Response(status=204)



