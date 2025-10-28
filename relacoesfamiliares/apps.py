"""Configuração do app Relações Familiares."""
from django.apps import AppConfig


class RelacoesFamiliaresConfig(AppConfig):
    """Configuração do aplicativo Relações Familiares."""
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relacoesfamiliares'
    verbose_name = 'Relações Familiares'
