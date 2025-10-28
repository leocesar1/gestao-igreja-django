"""Config do app Membros."""
from django.apps import AppConfig


class MembrosConfig(AppConfig):
    """Configuração do aplicativo Membros."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'membros'
    verbose_name = 'Membros'
