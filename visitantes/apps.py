"""Config do app Visitantes."""
from django.apps import AppConfig


class VisitantesConfig(AppConfig):
    """Configuração do aplicativo Visitantes."""
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'visitantes'
    verbose_name = 'Visitantes'
