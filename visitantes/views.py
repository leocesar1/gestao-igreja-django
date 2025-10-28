"""Views para Visitantes."""
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Visitante
from .serializers import VisitanteSerializer


class VisitanteViewSet(viewsets.ModelViewSet):
    """ViewSet para Visitantes."""
    
    queryset = Visitante.objects.select_related('pessoa', 'convidadopor').all()
    serializer_class = VisitanteSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'datavisita': ['gte', 'lte'],
        'foicontatado': ['exact'],
        'desejaretornar': ['exact']
    }
    search_fields = ['pessoa__nomecompleto', 'pessoa__telefone', 'origem']
    ordering_fields = ['datavisita', 'criadoem']
    ordering = ['-datavisita']
