"""Views para Usuários."""
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Usuario, CategoriaUsuario
from .serializers import UsuarioSerializer, UsuarioListSerializer, CategoriaUsuarioSerializer


class CategoriaUsuarioViewSet(viewsets.ModelViewSet):
    """ViewSet para Categoria de Usuário."""

    queryset = CategoriaUsuario.objects.all()
    serializer_class = CategoriaUsuarioSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nome', 'descricao']
    ordering_fields = ['nome', 'criado_em']
    ordering = ['nome']


class UsuarioViewSet(viewsets.ModelViewSet):
    """ViewSet para Usuário."""

    queryset = Usuario.objects.select_related('pessoa', 'categoria').all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'is_active': ['exact'],
        'is_staff': ['exact'],
        'categoria': ['exact'],
        'date_joined': ['gte', 'lte'],
    }
    search_fields = ['email', 'nome', 'pessoa__nome_completo']
    ordering_fields = ['email', 'nome', 'date_joined', 'criado_em']
    ordering = ['email']

    def get_serializer_class(self):
        """Retorna serializer apropriado para a a\u00e7\u00e3o."""
        if self.action == 'list':
            return UsuarioListSerializer
        return UsuarioSerializer
