"""URLs para Relações Familiares."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RelacaoFamiliarViewSet


router = DefaultRouter()
router.register(r'', RelacaoFamiliarViewSet, basename='relacaofamiliar')

app_name = 'relacoesfamiliares'

urlpatterns = [
    path('', include(router.urls)),
]
