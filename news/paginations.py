from rest_framework.pagination import PageNumberPagination


class NewsPagination(PageNumberPagination):
    page_size = 10