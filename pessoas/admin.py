"""Configuração do Django Admin para Pessoas."""
from django.contrib import admin
from .models import Pessoa


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    """Administração de Pessoas no Django Admin."""
    list_display = ('nome_completo', 'telefone', 'email', 'cidade', 'estado', 'ativo', 'criado_em')
    list_filter = ('ativo', 'sexo', 'estado', 'criado_em')
    search_fields = ('nome_completo', 'cpf', 'email', 'telefone', 'cidade')
    readonly_fields = ('id', 'criado_em', 'atualizado_em', 'idade')
    
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('id', 'nome_completo', 'data_nascimento', 'sexo', 'cpf')
        }),
        ('Contato', {
            'fields': ('telefone', 'telefone_secundario', 'email')
        }),
        ('Endereço', {
            'fields': ('cep', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'estado'),
            'classes': ('collapse',),
        }),
        ('Informações Adicionais', {
            'fields': ('observacoes', 'ativo')
        }),
        ('Auditoria', {
            'fields': ('criado_em', 'atualizado_em'),
            'classes': ('collapse',),
        }),
    )
    
    ordering = ('nome_completo',)
    date_hierarchy = 'criado_em'
