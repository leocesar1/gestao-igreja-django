"""Views para Relações Familiares."""
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import RelacaoFamiliar
from .serializers import RelacaoFamiliarSerializer, RelacaoFamiliarListSerializer


class RelacaoFamiliarViewSet(viewsets.ModelViewSet):
    """ViewSet para operações CRUD em Relação Familiar.
    
    Endpoints disponíveis:
    - GET /api/relacoes-familiares/ - Lista todas as relações
    - POST /api/relacoes-familiares/ - Cria nova relação
    - GET /api/relacoes-familiares/{id}/ - Detalhes de uma relação
    - PUT /api/relacoes-familiares/{id}/ - Atualiza relação completa
    - PATCH /api/relacoes-familiares/{id}/ - Atualiza campos específicos
    - DELETE /api/relacoes-familiares/{id}/ - Remove relação
    """
    
    queryset = RelacaoFamiliar.objects.select_related(
        'membro_origem__pessoa',
        'membro_destino__pessoa'
    ).all()
    
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    
    filterset_fields = {
        'tipo_relacao': ['exact'],
        'membro_origem': ['exact'],
        'membro_destino': ['exact'],
        'criado_em': ['gte', 'lte']
    }
    
    search_fields = [
        'membro_origem__pessoa__nome_completo',
        'membro_destino__pessoa__nome_completo',
        'observacoes'
    ]
    
    ordering_fields = [
        'criado_em',
        'tipo_relacao'
    ]
    
    ordering = ['-criado_em']
    
    def get_serializer_class(self):
        """Retorna serializer apropriado para a ação."""
        if self.action == 'list':
            return RelacaoFamiliarListSerializer
        return RelacaoFamiliarSerializer
