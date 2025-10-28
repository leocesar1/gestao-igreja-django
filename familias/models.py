"""Modelos para Famlias."""
import uuid
from django.db import models


class Familia(models.Model):
    """Modelo para agrupar membros em famlias."""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    nome = models.CharField(
        max_length=200,
        verbose_name="Nome da Famlia",
        help_text="Ex: Famlia Silva"
    )
    observacoes = models.TextField(
        blank=True,
        null=True,
        verbose_name="Observaes"
    )
    ativa = models.BooleanField(
        default=True,
        verbose_name="Ativa"
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Famlia"
        verbose_name_plural = "Famlias"
        ordering = ['nome']

    def __str__(self):
        return self.nome
