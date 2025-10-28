"""Testes para o app Visitantes."""
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from datetime import date
from pessoas.models import Pessoa
from .models import Visitante


@pytest.fixture
def api_client():
    """Fixture do cliente API."""
    return APIClient()


@pytest.fixture
def pessoa():
    """Fixture de pessoa para testes."""
    return Pessoa.objects.create(
        nomecompleto='Visitante Teste',
        telefone='11999999999',
        email='visitante@test.com'
    )


@pytest.mark.django_db
class TestVisitanteModel:
    """Testes do modelo Visitante."""
    
    def test_criar_visitante(self, pessoa):
        """Testa criação de visitante."""
        visitante = Visitante.objects.create(
            pessoa=pessoa,
            datavisita=date.today()
        )
        assert visitante.pessoa.nomecompleto == 'Visitante Teste'
        assert str(visitante) == 'Visitante: Visitante Teste'
    
    def test_visitante_properties(self, pessoa):
        """Testa propriedades do visitante."""
        visitante = Visitante.objects.create(
            pessoa=pessoa,
            datavisita=date.today()
        )
        assert visitante.nome == 'Visitante Teste'


@pytest.mark.django_db
class TestVisitanteAPI:
    """Testes da API de Visitantes."""
    
    def test_listar_visitantes(self, api_client, pessoa):
        """Testa listagem de visitantes."""
        Visitante.objects.create(
            pessoa=pessoa,
            datavisita=date.today()
        )
        url = reverse('visitantes:visitante-list')
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
