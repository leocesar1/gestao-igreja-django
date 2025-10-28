"""Modelos do app Pessoas."""
import uuid
from django.db import models
from django.core.validators import RegexValidator


class Pessoa(models.Model):
    """Modelo base para representar uma pessoa no sistema.
    
    Contém informações básicas compartilhadas entre membros e visitantes.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="ID")
    nome_completo = models.CharField(max_length=200, verbose_name="Nome Completo")
    
    telefone_validator = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Formato inválido. Use: 999999999")
    telefone = models.CharField(validators=[telefone_validator], max_length=17, blank=True, null=True, verbose_name="Telefone")
    telefone_secundario = models.CharField(validators=[telefone_validator], max_length=17, blank=True, null=True, verbose_name="Telefone Secundário")
    email = models.EmailField(max_length=254, blank=True, null=True, verbose_name="E-mail")
    
    cpf_validator = RegexValidator(regex=r'^\d{11}$', message="CPF deve ter 11 dígitos")
    cpf = models.CharField(validators=[cpf_validator], max_length=11, blank=True, null=True, unique=True, verbose_name="CPF")
    
    data_nascimento = models.DateField(blank=True, null=True, verbose_name="Data de Nascimento")
    
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=True, null=True)
    
    # Endereço
    cep = models.CharField(max_length=8, blank=True, null=True, verbose_name="CEP")
    logradouro = models.CharField(max_length=255, blank=True, null=True)
    numero = models.CharField(max_length=10, blank=True, null=True)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=2, blank=True, null=True)
    
    observacoes = models.TextField(blank=True, null=True)
    
    # Auditoria
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
        ordering = ['nome_completo']
        indexes = [
            models.Index(fields=['nome_completo']),
            models.Index(fields=['cpf']),
        ]
    
    def __str__(self):
        return self.nome_completo
    
    @property
    def endereco_completo(self):
        """Retorna endereço formatado."""
        partes = []
        if self.logradouro:
            end = self.logradouro
            if self.numero:
                end = f"{end}, {self.numero}"
            if self.complemento:
                end = f"{end} - {self.complemento}"
            partes.append(end)
        if self.bairro:
            partes.append(self.bairro)
        if self.cidade and self.estado:
            partes.append(f"{self.cidade}/{self.estado}")
        if self.cep:
            partes.append(f"CEP {self.cep}")
        return " - ".join(partes) if partes else "Não cadastrado"
    
    @property
    def idade(self):
        """Calcula idade baseada na data de nascimento."""
        if not self.data_nascimento:
            return None
        from datetime import date
        hoje = date.today()
        idade = hoje.year - self.data_nascimento.year
        if (hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day):
            idade -= 1
        return idade
