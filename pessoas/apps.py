"""Configuração do app Pessoas."""
from django.apps import AppConfig


class PessoasConfig(AppConfig):
    """Configuração do aplicativo Pessoas."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pessoas'
    verbose_name = 'Pessoas'
