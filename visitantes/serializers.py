"""Serializers para Visitantes."""
from rest_framework import serializers
from .models import Visitante
from pessoas.serializers import PessoaSerializer


class VisitanteSerializer(serializers.ModelSerializer):
    """Serializer para Visitante com dados da pessoa."""
    
    pessoa_detalhes = PessoaSerializer(source='pessoa', read_only=True)
    nome = serializers.ReadOnlyField()
    convidadopor_nome = serializers.CharField(
        source='convidadopor.nome',
        read_only=True
    )
    
    class Meta:
        model = Visitante
        fields = '__all__'
        read_only_fields = ('id', 'criadoem', 'atualizadoem')
