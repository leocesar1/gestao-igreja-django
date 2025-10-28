"""Serializers do app Famlias."""
from rest_framework import serializers
from .models import Familia


class FamiliaSerializer(serializers.ModelSerializer):
    """Serializer completo para Famlia."""

    class Meta:
        model = Familia
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'atualizado_em')


class FamiliaListSerializer(serializers.ModelSerializer):
    """Serializer simplificado para listagem."""

    class Meta:
        model = Familia
        fields = ('id', 'nome', 'ativa')
