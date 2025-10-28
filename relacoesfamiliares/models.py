"""Modelos para Relações Familiares."""
import uuid
from django.db import models
from membros.models import Membro


class RelacaoFamiliar(models.Model):
    """Modelo para vínculos familiares entre membros."""
    
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    
    membro_origem = models.ForeignKey(
        Membro,
        on_delete=models.CASCADE,
        related_name='relacoes_origem',
        verbose_name='Membro Origem'
    )
    
    membro_destino = models.ForeignKey(
        Membro,
        on_delete=models.CASCADE,
        related_name='relacoes_destino',
        verbose_name='Membro Destino'
    )
    
    TIPO_RELACAO_CHOICES = [
        ('pai', 'Pai/Mãe'),
        ('filho', 'Filho/Filha'),
        ('conjuge', 'Cônjuge'),
        ('irmao', 'Irmão/Irmã'),
        ('avo', 'Avô/Avó'),
        ('neto', 'Neto/Neta'),
        ('tio', 'Tio/Tia'),
        ('sobrinho', 'Sobrinho/Sobrinha'),
        ('outro', 'Outro'),
    ]
    
    tipo_relacao = models.CharField(
        max_length=20,
        choices=TIPO_RELACAO_CHOICES,
        verbose_name='Tipo de Relação'
    )
    
    observacoes = models.TextField(
        blank=True,
        null=True,
        verbose_name='Observações'
    )
    
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Relação Familiar'
        verbose_name_plural = 'Relações Familiares'
        unique_together = ['membro_origem', 'membro_destino', 'tipo_relacao']
    
    def __str__(self):
        return f"{self.membro_origem.nome} - {self.get_tipo_relacao_display()} - {self.membro_destino.nome}"
