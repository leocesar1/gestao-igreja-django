"""URLs para Visitantes."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VisitanteViewSet

router = DefaultRouter()
router.register(r'', VisitanteViewSet, basename='visitante')

app_name = 'visitantes'

urlpatterns = [
    path('', include(router.urls)),
]
