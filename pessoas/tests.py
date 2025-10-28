"""Testes para o app Pessoas."""
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Pessoa


@pytest.fixture
def api_client():
    """Fixture do cliente API."""
    return APIClient()


@pytest.fixture
def pessoa_data():
    """Fixture com dados de pessoa."""
    return {
        'nome_completo': 'João Silva',
        'telefone': '11987654321',
        'email': 'joao@example.com',
        'cpf': '12345678901',
        'data_nascimento': '1990-01-15',
        'sexo': 'M',
        'cidade': 'São Paulo',
        'estado': 'SP',
        'ativo': True
    }


@pytest.mark.django_db
class TestPessoaModel:
    """Testes do modelo Pessoa."""
    
    def test_criar_pessoa(self, pessoa_data):
        """Testa criação de pessoa."""
        pessoa = Pessoa.objects.create(**pessoa_data)
        assert pessoa.nome_completo == 'João Silva'
        assert pessoa.ativo is True
        assert str(pessoa) == 'João Silva'
    
    def test_idade_property(self):
        """Testa cálculo de idade."""
        from datetime import date
        pessoa = Pessoa.objects.create(
            nome_completo='Teste',
            data_nascimento=date(1990, 1, 1)
        )
        assert pessoa.idade >= 33


@pytest.mark.django_db
class TestPessoaAPI:
    """Testes da API de Pessoas."""
    
    def test_listar_pessoas(self, api_client, pessoa_data):
        """Testa listagem de pessoas."""
        Pessoa.objects.create(**pessoa_data)
        url = reverse('pessoas:pessoa-list')
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
    
    def test_criar_pessoa_api(self, api_client, pessoa_data):
        """Testa criação via API."""
        url = reverse('pessoas:pessoa-list')
        response = api_client.post(url, pessoa_data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert Pessoa.objects.count() == 1
