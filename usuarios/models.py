"""Modelo de Usuário Customizado."""
import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _


class UsuarioManager(BaseUserManager):
    """Manager customizado para o modelo Usuario."""

    def create_user(self, email, password=None, **extra_fields):
        """Cria e salva um usuário comum."""
        if not email:
            raise ValueError('O email é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Cria e salva um superusuário."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superusuário deve ter is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superusuário deve ter is_superuser=True')

        return self.create_user(email, password, **extra_fields)


class CategoriaUsuario(models.Model):
    """Categorias de usuários com permissões específicas."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100, unique=True, verbose_name='Nome')
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')

    # Permissões específicas
    pode_gerenciar_membros = models.BooleanField(default=False)
    pode_gerenciar_financas = models.BooleanField(default=False)
    pode_gerenciar_eventos = models.BooleanField(default=False)
    pode_visualizar_relatorios = models.BooleanField(default=False)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Categoria de Usuário'
        verbose_name_plural = 'Categorias de Usuários'

    def __str__(self):
        return self.nome


class Usuario(AbstractBaseUser, PermissionsMixin):
    """Modelo de usuário customizado usando email como identificador."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField('email', unique=True)
    nome = models.CharField('nome', max_length=150, blank=True)
    pessoa = models.OneToOneField(
        'pessoas.Pessoa',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='usuario',
        verbose_name='Pessoa Vinculada'
    )
    categoria = models.ForeignKey(
        CategoriaUsuario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='usuarios',
        verbose_name='Categoria'
    )
    is_staff = models.BooleanField('staff', default=False)
    is_active = models.BooleanField('ativo', default=True)
    date_joined = models.DateTimeField('data de cadastro', auto_now_add=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.nome

    def get_short_name(self):
        return self.nome
