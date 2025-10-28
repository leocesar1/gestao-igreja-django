"""Signals para sincroniza\u00e7\u00e3o Pessoa Usuario."""
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .models import Usuario


@receiver(post_save, sender=Usuario, dispatch_uid='criar_token_usuario')
def criar_token_para_usuario(sender, instance, created, **kwargs):
    """Cria token de autentica\u00e7\u00e3o quando usu\u00e1rio \u00e9 criado."""
    if created:
        Token.objects.create(user=instance)
