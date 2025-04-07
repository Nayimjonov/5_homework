from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


router = DefaultRouter()
router.register(r'news', views.NewsViewSet, basename='news')

urlpatterns = [
    path('', include(router.urls)),
]