"""Modelos do app Membros."""
import uuid
from django.db import models
from pessoas.models import Pessoa


class Membro(models.Model):
    """Modelo que estende Pessoa com informações eclesiásticas.
    
    Relacionamento 1:1 com Pessoa.
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    pessoa = models.OneToOneField(
        Pessoa,
        on_delete=models.CASCADE,
        related_name='membro',
        verbose_name='Pessoa'
    )
    
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('afastado', 'Afastado'),
        ('transferido', 'Transferido'),
        ('disciplinado', 'Disciplinado'),
        ('falecido', 'Falecido'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='ativo',
        verbose_name='Status'
    )
    
    data_batismo = models.DateField(
        blank=True,
        null=True,
        verbose_name='Data de Batismo'
    )
    data_admissao = models.DateField(
        blank=True,
        null=True,
        verbose_name='Data de Admissão'
    )
    
    FORMA_ADMISSAO_CHOICES = [
        ('batismo', 'Batismo'),
        ('aclamacao', 'Aclamação'),
        ('transferencia', 'Transferência'),
        ('reconciliacao', 'Reconciliação'),
    ]
    forma_admissao = models.CharField(
        max_length=20,
        choices=FORMA_ADMISSAO_CHOICES,
        blank=True,
        null=True,
        verbose_name='Forma de Admissão'
    )
    
    igreja_origem = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Igreja de Origem'
    )
    cargo = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Cargo',
        help_text='Ex: Pastor, Presbítero, Diácono'
    )
    dons_espirituais = models.TextField(
        blank=True,
        null=True,
        verbose_name='Dons Espirituais'
    )
    foto = models.ImageField(
        upload_to='membros/fotos/',
        blank=True,
        null=True,
        verbose_name='Foto'
    )
    
    # Auditoria
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Membro'
        verbose_name_plural = 'Membros'
        ordering = ['pessoa__nome_completo']
    
    def __str__(self):
        return f'Membro: {self.pessoa.nome_completo}'
    
    @property
    def nome(self):
        """Retorna nome da pessoa."""
        return self.pessoa.nome_completo
    
    @property
    def esta_ativo(self):
        """Verifica se membro está ativo."""
        return self.status == 'ativo'
