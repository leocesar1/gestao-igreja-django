"""URLs para Usuários."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, CategoriaUsuarioViewSet

router = DefaultRouter()
router.register(r'', UsuarioViewSet, basename='usuario')
router.register(r'categorias', CategoriaUsuarioViewSet, basename='categoria-usuario')

app_name = 'usuarios'

urlpatterns = [
    path('', include(router.urls)),
]
