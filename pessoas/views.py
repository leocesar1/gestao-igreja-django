"""Views do app Pessoas."""
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Pessoa
from .serializers import PessoaSerializer, PessoaListSerializer


class PessoaViewSet(viewsets.ModelViewSet):
    """ViewSet para operações CRUD em Pessoa.
    
    Endpoints disponíveis:
    - GET /api/pessoas/ - Lista todas as pessoas
    - POST /api/pessoas/ - Cria nova pessoa
    - GET /api/pessoas/<id>/ - Detalhes de uma pessoa
    - PUT /api/pessoas/<id>/ - Atualiza pessoa completa
    - PATCH /api/pessoas/<id>/ - Atualiza campos específicos
    - DELETE /api/pessoas/<id>/ - Remove pessoa
    """
    queryset = Pessoa.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'ativo': ['exact'],
        'sexo': ['exact'],
        'cidade': ['exact', 'icontains'],
        'estado': ['exact'],
        'data_nascimento': ['gte', 'lte'],
    }
    search_fields = ['nome_completo', 'cpf', 'email', 'telefone', 'cidade']
    ordering_fields = ['nome_completo', 'criado_em', 'data_nascimento']
    ordering = ['nome_completo']
    
    def get_serializer_class(self):
        """Retorna serializer apropriado para a ação."""
        if self.action == 'list':
            return PessoaListSerializer
        return PessoaSerializer
