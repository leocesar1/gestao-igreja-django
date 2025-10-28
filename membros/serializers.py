"""Serializers para Membros."""
from rest_framework import serializers
from .models import Membro
from pessoas.serializers import PessoaSerializer


class MembroSerializer(serializers.ModelSerializer):
    """Serializer para Membro com dados da pessoa."""
    pessoa_detalhes = PessoaSerializer(source='pessoa', read_only=True)
    nome = serializers.ReadOnlyField()
    esta_ativo = serializers.ReadOnlyField()
    
    class Meta:
        model = Membro
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'atualizado_em')


class MembroListSerializer(serializers.ModelSerializer):
    """Serializer simplificado para listagem."""
    nome = serializers.CharField(source='pessoa.nome_completo')
    telefone = serializers.CharField(source='pessoa.telefone')
    
    class Meta:
        model = Membro
        fields = ('id', 'nome', 'telefone', 'status', 'cargo', 'data_admissao')
