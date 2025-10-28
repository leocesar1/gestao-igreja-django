"""Configurao do Django Admin para Famlias."""
from django.contrib import admin
from .models import Familia


@admin.register(Familia)
class FamiliaAdmin(admin.ModelAdmin):
    """Administrao de Famlias no Django Admin."""

    list_display = ('nome', 'ativa', 'criado_em')
    list_filter = ('ativa', 'criado_em')
    search_fields = ('nome',)
    readonly_fields = ('id', 'criado_em', 'atualizado_em')
    fieldsets = (
        ('Informaes Bsicas', {
            'fields': ('id', 'nome', 'ativa')
        }),
        ('Observaes', {
            'fields': ('observacoes',),
            'classes': ('collapse',)
        }),
        ('Auditoria', {
            'fields': ('criado_em', 'atualizado_em'),
            'classes': ('collapse',)
        }),
    )
    ordering = ('nome',)
    date_hierarchy = 'criado_em'
