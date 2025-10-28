"""Serializers para Usuários."""
from rest_framework import serializers
from .models import Usuario, CategoriaUsuario
from pessoas.serializers import PessoaSerializer


class CategoriaUsuarioSerializer(serializers.ModelSerializer):
    """Serializer para Categoria de Usuário."""

    class Meta:
        model = CategoriaUsuario
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'atualizado_em')


class UsuarioSerializer(serializers.ModelSerializer):
    """Serializer completo para Usuário."""

    pessoa_detalhes = PessoaSerializer(source='pessoa', read_only=True)
    categoria_detalhes = CategoriaUsuarioSerializer(source='categoria', read_only=True)

    class Meta:
        model = Usuario
        fields = (
            'id', 'email', 'nome', 'pessoa', 'pessoa_detalhes',
            'categoria', 'categoria_detalhes', 'is_staff', 'is_active',
            'date_joined', 'criado_em', 'atualizado_em'
        )
        read_only_fields = ('id', 'date_joined', 'criado_em', 'atualizado_em')
        extra_kwargs = {'password': {'write_only': True}}


class UsuarioListSerializer(serializers.ModelSerializer):
    """Serializer simplificado para listagem de Usuários."""

    categoria_nome = serializers.CharField(source='categoria.nome', read_only=True)

    class Meta:
        model = Usuario
        fields = ('id', 'email', 'nome', 'categoria_nome', 'is_active', 'is_staff')
