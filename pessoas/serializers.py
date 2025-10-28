"""Serializers do app Pessoas."""
from rest_framework import serializers
from .models import Pessoa


class PessoaSerializer(serializers.ModelSerializer):
    """Serializer completo para Pessoa."""
    idade = serializers.ReadOnlyField()
    endereco_completo = serializers.ReadOnlyField()
    
    class Meta:
        model = Pessoa
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'atualizado_em')
    
    def validate_cpf(self, value):
        """Valida formato do CPF."""
        if value and len(value) != 11:
            raise serializers.ValidationError("CPF deve ter 11 dígitos")
        return value


class PessoaListSerializer(serializers.ModelSerializer):
    """Serializer simplificado para listagem."""
    
    class Meta:
        model = Pessoa
        fields = ('id', 'nome_completo', 'telefone', 'email', 'cidade', 'estado', 'ativo')
