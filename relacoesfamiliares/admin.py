"""Admin para Relações Familiares."""
from django.contrib import admin
from .models import RelacaoFamiliar


@admin.register(RelacaoFamiliar)
class RelacaoFamiliarAdmin(admin.ModelAdmin):
    """Administração de Relações Familiares."""
    
    list_display = (
        'get_membro_origem',
        'tipo_relacao',
        'get_membro_destino',
        'criado_em'
    )
    
    list_filter = (
        'tipo_relacao',
        'criado_em'
    )
    
    search_fields = (
        'membro_origem__pessoa__nome_completo',
        'membro_destino__pessoa__nome_completo'
    )
    
    readonly_fields = (
        'id',
        'criado_em',
        'atualizado_em'
    )
    
    autocomplete_fields = [
        'membro_origem',
        'membro_destino'
    ]
    
    fieldsets = (
        ('Relação', {
            'fields': (
                'id',
                'membro_origem',
                'membro_destino',
                'tipo_relacao'
            )
        }),
        ('Informações Adicionais', {
            'fields': ('observacoes',)
        }),
        ('Auditoria', {
            'fields': ('criado_em', 'atualizado_em'),
            'classes': ('collapse',)
        }),
    )
    
    ordering = ('-criado_em',)
    date_hierarchy = 'criado_em'
    
    def get_membro_origem(self, obj):
        """Retorna nome do membro origem."""
        return obj.membro_origem.nome
    get_membro_origem.short_description = 'Membro Origem'
    get_membro_origem.admin_order_field = 'membro_origem__pessoa__nome_completo'
    
    def get_membro_destino(self, obj):
        """Retorna nome do membro destino."""
        return obj.membro_destino.nome
    get_membro_destino.short_description = 'Membro Destino'
    get_membro_destino.admin_order_field = 'membro_destino__pessoa__nome_completo'
