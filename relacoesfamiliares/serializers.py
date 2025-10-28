"""Serializers para Relações Familiares."""
from rest_framework import serializers
from .models import RelacaoFamiliar
from membros.serializers import MembroListSerializer


class RelacaoFamiliarSerializer(serializers.ModelSerializer):
    """Serializer completo para Relação Familiar."""
    
    membro_origem_detalhes = MembroListSerializer(
        source='membro_origem',
        read_only=True
    )
    
    membro_destino_detalhes = MembroListSerializer(
        source='membro_destino',
        read_only=True
    )
    
    tipo_relacao_display = serializers.CharField(
        source='get_tipo_relacao_display',
        read_only=True
    )
    
    class Meta:
        model = RelacaoFamiliar
        fields = '__all__'
        read_only_fields = ('id', 'criado_em', 'atualizado_em')
    
    def validate(self, data):
        """Valida a relação familiar."""
        # Verifica se não está criando relação de um membro consigo mesmo
        if data.get('membro_origem') == data.get('membro_destino'):
            raise serializers.ValidationError(
                "Um membro não pode ter relação familiar consigo mesmo."
            )
        return data


class RelacaoFamiliarListSerializer(serializers.ModelSerializer):
    """Serializer simplificado para listagem."""
    
    membro_origem_nome = serializers.CharField(
        source='membro_origem.nome',
        read_only=True
    )
    
    membro_destino_nome = serializers.CharField(
        source='membro_destino.nome',
        read_only=True
    )
    
    tipo_relacao_display = serializers.CharField(
        source='get_tipo_relacao_display',
        read_only=True
    )
    
    class Meta:
        model = RelacaoFamiliar
        fields = [
            'id',
            'membro_origem_nome',
            'membro_destino_nome',
            'tipo_relacao',
            'tipo_relacao_display',
            'criado_em'
        ]
