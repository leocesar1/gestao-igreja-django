"""Modelos para Visitantes."""
import uuid
from django.db import models
from pessoas.models import Pessoa
from membros.models import Membro


class Visitante(models.Model):
    """Modelo para visitantes da igreja."""
    
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    pessoa = models.OneToOneField(
        Pessoa,
        on_delete=models.CASCADE,
        related_name='visitante',
        verbose_name='Pessoa'
    )
    datavisita = models.DateField(
        verbose_name='Data da Visita',
        help_text='Data da primeira visita'
    )
    convidadopor = models.ForeignKey(
        Membro,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='visitantes_convidados',
        verbose_name='Convidado por'
    )
    origem = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Origem',
        help_text='Como conheceu a igreja'
    )
    interesse = models.TextField(
        blank=True,
        null=True,
        verbose_name='Interesse',
        help_text='Áreas de interesse ou necessidades'
    )
    foicontatado = models.BooleanField(
        default=False,
        verbose_name='Foi Contatado'
    )
    datacontato = models.DateField(
        blank=True,
        null=True,
        verbose_name='Data do Contato'
    )
    desejaretornar = models.BooleanField(
        default=True,
        verbose_name='Deseja Retornar'
    )
    criadoem = models.DateTimeField(auto_now_add=True)
    atualizadoem = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Visitante'
        verbose_name_plural = 'Visitantes'
        ordering = ['-datavisita']
    
    def __str__(self):
        return f"Visitante: {self.pessoa.nomecompleto}"
    
    @property
    def nome(self):
        return self.pessoa.nomecompleto
