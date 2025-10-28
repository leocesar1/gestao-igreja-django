"""Testes para o app Famlias."""
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Familia


@pytest.fixture
def api_client():
    """Fixture do cliente API."""
    return APIClient()


@pytest.fixture
def familia_data():
    """Fixture com dados de famlia."""
    return {
        'nome': 'Famlia Silva',
        'ativa': True,
        'observacoes': 'Famlia cadastrada para testes'
    }


@pytest.mark.django_db
class TestFamiliaModel:
    """Testes do modelo Famlia."""

    def test_criar_familia(self, familia_data):
        """Testa criao de famlia."""
        familia = Familia.objects.create(**familia_data)
        assert familia.nome == 'Famlia Silva'
        assert familia.ativa is True
        assert str(familia) == 'Famlia Silva'


@pytest.mark.django_db
class TestFamiliaAPI:
    """Testes da API de Famlias."""

    def test_listar_familias(self, api_client, familia_data):
        """Testa listagem de famlias."""
        Familia.objects.create(**familia_data)
        url = reverse('familias:familia-list')
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_criar_familia_api(self, api_client, familia_data):
        """Testa criao via API."""
        url = reverse('familias:familia-list')
        response = api_client.post(url, familia_data, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert Familia.objects.count() == 1
