"""Testes para o app Membros."""
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from pessoas.models import Pessoa
from .models import Membro


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


@pytest.fixture
def pessoa(pessoa_data):
    """Fixture que cria uma pessoa."""
    return Pessoa.objects.create(**pessoa_data)


@pytest.fixture
def membro_data(pessoa):
    """Fixture com dados de membro."""
    return {
        'pessoa': pessoa,
        'status': 'ativo',
        'data_batismo': '2010-05-20',
        'data_admissao': '2010-06-15',
        'forma_admissao': 'batismo',
        'cargo': 'Diácono'
    }


@pytest.mark.django_db
class TestMembroModel:
    """Testes do modelo Membro."""
    
    def test_criar_membro(self, membro_data):
        """Testa criação de membro."""
        membro = Membro.objects.create(**membro_data)
        assert membro.pessoa.nome_completo == 'João Silva'
        assert membro.status == 'ativo'
        assert str(membro) == 'Membro: João Silva'
    
    def test_nome_property(self, membro_data):
        """Testa property nome."""
        membro = Membro.objects.create(**membro_data)
        assert membro.nome == 'João Silva'
    
    def test_esta_ativo_property(self, membro_data):
        """Testa property esta_ativo."""
        membro = Membro.objects.create(**membro_data)
        assert membro.esta_ativo is True
        
        membro.status = 'afastado'
        membro.save()
        assert membro.esta_ativo is False


@pytest.mark.django_db
class TestMembroAPI:
    """Testes da API de Membros."""
    
    def test_listar_membros(self, api_client, membro_data):
        """Testa listagem de membros."""
        Membro.objects.create(**membro_data)
        url = reverse('membros:membro-list')
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 1
    
    def test_criar_membro_api(self, api_client, pessoa):
        """Testa criação via API."""
        url = reverse('membros:membro-list')
        data = {
            'pessoa': str(pessoa.id),
            'status': 'ativo',
            'data_batismo': '2010-05-20',
            'data_admissao': '2010-06-15',
            'forma_admissao': 'batismo',
            'cargo': 'Diácono'
        }
        response = api_client.post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert Membro.objects.count() == 1
    
    def test_filtrar_por_status(self, api_client, membro_data):
        """Testa filtro por status."""
        Membro.objects.create(**membro_data)
        url = reverse('membros:membro-list')
        response = api_client.get(url, {'status': 'ativo'})
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 1
