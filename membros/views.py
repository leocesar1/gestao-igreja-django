"""Views para Membros."""
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Membro
from .serializers import MembroSerializer, MembroListSerializer


class MembroViewSet(viewsets.ModelViewSet):
    """ViewSet para Membros."""
    queryset = Membro.objects.select_related('pessoa').all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'status': ['exact'],
        'cargo': ['exact', 'icontains'],
        'forma_admissao': ['exact'],
        'data_admissao': ['gte', 'lte'],
        'data_batismo': ['gte', 'lte'],
    }
    search_fields = [
        'pessoa__nome_completo',
        'pessoa__cpf',
        'cargo',
        'igreja_origem'
    ]
    ordering_fields = ['pessoa__nome_completo', 'data_admissao', 'criado_em']
    ordering = ['pessoa__nome_completo']
    
    def get_serializer_class(self):
        if self.action == 'list':
            return MembroListSerializer
        return MembroSerializer
