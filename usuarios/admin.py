"""Admin para Usuários."""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Usuario, CategoriaUsuario


@admin.register(CategoriaUsuario)
class CategoriaUsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'pode_gerenciar_membros', 'pode_gerenciar_financas', 'criado_em')
    search_fields = ('nome',)


@admin.register(Usuario)
class UsuarioAdmin(BaseUserAdmin):
    list_display = ('email', 'nome', 'categoria', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_active', 'categoria', 'date_joined')
    search_fields = ('email', 'nome')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informa\u00e7\u00f5es Pessoais', {'fields': ('nome', 'pessoa')}),
        ('Permiss\u00f5es', {'fields': ('categoria', 'is_active', 'is_staff', 'is_superuser')}),
        ('Datas', {'fields': ('date_joined', 'last_login')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'nome', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
