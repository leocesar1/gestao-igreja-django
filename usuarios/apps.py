"""Config do app Usuarios."""
from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuarios'
    verbose_name = 'Usu\u00e1rios'

    def ready(self):
        """Importa signals quando app est\u00e1 pronto."""
        import usuarios.signals
