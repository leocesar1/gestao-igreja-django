"""Configurao do app Famlias."""
from django.apps import AppConfig


class FamiliasConfig(AppConfig):
    """Configurao do aplicativo Famlias."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'familias'
    verbose_name = 'Famlias'
