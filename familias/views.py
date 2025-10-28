"""Views do app Famlias."""
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Familia
from .serializers import FamiliaSerializer, FamiliaListSerializer


class FamiliaViewSet(viewsets.ModelViewSet):
    """
    ViewSet para operaes CRUD em Famlia.

    Endpoints disponveis:
    - GET /api/familias/ - Lista todas as famlias
    - POST /api/familias/ - Cria nova famlia
    - GET /api/familias/{id}/ - Detalhes de uma famlia
    - PUT /api/familias/{id}/ - Atualiza famlia completa
    - PATCH /api/familias/{id}/ - Atualiza campos especficos
    - DELETE /api/familias/{id}/ - Remove famlia
    """

    queryset = Familia.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {'ativa': ['exact']}
    search_fields = ['nome']
    ordering_fields = ['nome', 'criado_em']
    ordering = ['nome']

    def get_serializer_class(self):
        """Retorna serializer apropriado para a ao."""
        if self.action == 'list':
            return FamiliaListSerializer
        return FamiliaSerializer
