"""URLs para Membros."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MembroViewSet


router = DefaultRouter()
router.register(r'', MembroViewSet, basename='membro')

app_name = 'membros'

urlpatterns = [
    path('', include(router.urls)),
]
