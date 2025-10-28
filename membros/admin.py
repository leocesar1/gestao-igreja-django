"""Admin para Membros."""
from django.contrib import admin
from .models import Membro


@admin.register(Membro)
class MembroAdmin(admin.ModelAdmin):
    """Administração de Membros."""
    list_display = (
        'get_nome',
        'status',
        'cargo',
        'data_admissao',
        'data_batismo',
        'criado_em'
    )
    list_filter = ('status', 'forma_admissao', 'cargo', 'data_admissao')
    search_fields = (
        'pessoa__nome_completo',
        'pessoa__cpf',
        'cargo',
        'igreja_origem'
    )
    readonly_fields = ('id', 'criado_em', 'atualizado_em')
    autocomplete_fields = ['pessoa']
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('id', 'pessoa', 'status', 'foto')
        }),
        ('Informações Eclesiásticas', {
            'fields': (
                'data_batismo',
                'data_admissao',
                'forma_admissao',
                'igreja_origem',
                'cargo',
                'dons_espirituais'
            )
        }),
        ('Auditoria', {
            'fields': ('criado_em', 'atualizado_em'),
            'classes': ('collapse',)
        }),
    )
    
    def get_nome(self, obj):
        """Retorna nome do membro."""
        return obj.pessoa.nome_completo
    get_nome.short_description = 'Nome'
    get_nome.admin_order_field = 'pessoa__nome_completo'
