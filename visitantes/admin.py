"""Admin para Visitantes."""
from django.contrib import admin
from .models import Visitante


@admin.register(Visitante)
class VisitanteAdmin(admin.ModelAdmin):
    list_display = ('get_nome', 'datavisita', 'get_convidadopor', 'foicontatado', 'desejaretornar')
    list_filter = ('datavisita', 'foicontatado', 'desejaretornar', 'criadoem')
    search_fields = ('pessoa__nomecompleto', 'pessoa__telefone', 'origem')
    readonly_fields = ('id', 'criadoem', 'atualizadoem')
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('id', 'pessoa', 'datavisita')
        }),
        ('Origem e Convite', {
            'fields': ('convidadopor', 'origem', 'interesse')
        }),
        ('Acompanhamento', {
            'fields': ('foicontatado', 'datacontato', 'desejaretornar')
        }),
        ('Auditoria', {
            'fields': ('criadoem', 'atualizadoem'),
            'classes': ('collapse',)
        }),
    )
    
    def get_nome(self, obj):
        """Retorna nome do visitante."""
        return obj.pessoa.nomecompleto
    get_nome.short_description = 'Nome'
    
    def get_convidadopor(self, obj):
        return obj.convidadopor.nome if obj.convidadopor else '-'
    get_convidadopor.short_description = 'Convidado por'
