"""Testes para o app Usuarios."""
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Usuario, CategoriaUsuario


@pytest.fixture
def api_client():
    """Fixture do cliente API."""
    return APIClient()


@pytest.fixture
def categoria_usuario():
    """Fixture de categoria de usu\u00e1rio."""
    return CategoriaUsuario.objects.create(
        nome='Pastor',
        descricao='Acesso total',
        pode_gerenciar_membros=True,
        pode_gerenciar_financas=True,
        pode_gerenciar_eventos=True,
        pode_visualizar_relatorios=True
    )


@pytest.fixture
def usuario_data():
    """Fixture com dados de usu\u00e1rio."""
    return {
        'email': 'teste@example.com',
        'nome': 'Usu\u00e1rio Teste',
        'is_active': True
    }


@pytest.mark.django_db
class TestUsuarioModel:
    """Testes do modelo Usuario."""

    def test_criar_usuario(self, usuario_data):
        """Testa cria\u00e7\u00e3o de usu\u00e1rio."""
        usuario = Usuario.objects.create_user(
            email=usuario_data['email'],
            password='senha123',
            nome=usuario_data['nome']
        )
        assert usuario.email == usuario_data['email']
        assert usuario.is_active is True
        assert str(usuario) == usuario_data['email']

    def test_criar_superusuario(self):
        """Testa cria\u00e7\u00e3o de superusu\u00e1rio."""
        admin = Usuario.objects.create_superuser(
            email='admin@example.com',
            password='admin123',
            nome='Admin'
        )
        assert admin.is_staff is True
        assert admin.is_superuser is True
        assert admin.is_active is True


@pytest.mark.django_db
class TestCategoriaUsuarioModel:
    """Testes do modelo CategoriaUsuario."""

    def test_criar_categoria(self, categoria_usuario):
        """Testa cria\u00e7\u00e3o de categoria."""
        assert categoria_usuario.nome == 'Pastor'
        assert categoria_usuario.pode_gerenciar_membros is True
        assert str(categoria_usuario) == 'Pastor'


@pytest.mark.django_db
class TestUsuarioAPI:
    """Testes da API de Usuarios."""

    def test_listar_usuarios(self, api_client, usuario_data):
        """Testa listagem de usu\u00e1rios."""
        Usuario.objects.create_user(
            email=usuario_data['email'],
            password='senha123',
            nome=usuario_data['nome']
        )
        url = reverse('usuarios:usuario-list')
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
