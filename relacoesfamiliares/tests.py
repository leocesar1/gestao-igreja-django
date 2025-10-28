"""Testes para o app Relações Familiares."""
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import RelacaoFamiliar
from membros.models import Membro
from pessoas.models import Pessoa


@pytest.fixture
def api_client():
    """Fixture do cliente API."""
    return APIClient()


@pytest.fixture
def pessoa_origem():
    """Fixture de pessoa origem."""
    return Pessoa.objects.create(
        nome_completo='João Silva',
        cpf='12345678901',
        data_nascimento='1970-01-15',
        sexo='M'
    )


@pytest.fixture
def pessoa_destino():
    """Fixture de pessoa destino."""
    return Pessoa.objects.create(
        nome_completo='Maria Silva',
        cpf='98765432100',
        data_nascimento='2000-05-20',
        sexo='F'
    )


@pytest.fixture
def membro_origem(pessoa_origem):
    """Fixture de membro origem."""
    return Membro.objects.create(
        pessoa=pessoa_origem,
        status='ativo',
        data_admissao='2010-01-01'
    )


@pytest.fixture
def membro_destino(pessoa_destino):
    """Fixture de membro destino."""
    return Membro.objects.create(
        pessoa=pessoa_destino,
        status='ativo',
        data_admissao='2018-06-15'
    )


@pytest.fixture
def relacao_data(membro_origem, membro_destino):
    """Fixture com dados de relação familiar."""
    return {
        'membro_origem': membro_origem.id,
        'membro_destino': membro_destino.id,
        'tipo_relacao': 'pai',
        'observacoes': 'Teste de relação pai e filha'
    }


@pytest.mark.django_db
class TestRelacaoFamiliarModel:
    """Testes do modelo RelacaoFamiliar."""
    
    def test_criar_relacao_familiar(self, membro_origem, membro_destino):
        """Testa criação de relação familiar."""
        relacao = RelacaoFamiliar.objects.create(
            membro_origem=membro_origem,
            membro_destino=membro_destino,
            tipo_relacao='pai'
        )
        
        assert relacao.membro_origem == membro_origem
        assert relacao.membro_destino == membro_destino
        assert relacao.tipo_relacao == 'pai'
        assert 'João Silva' in str(relacao)
        assert 'Maria Silva' in str(relacao)
    
    def test_tipos_relacao_disponiveis(self):
        """Testa tipos de relação disponíveis."""
        tipos_esperados = [
            'pai', 'filho', 'conjuge', 'irmao',
            'avo', 'neto', 'tio', 'sobrinho', 'outro'
        ]
        
        tipos_choices = [choice[0] for choice in RelacaoFamiliar.TIPO_RELACAO_CHOICES]
        
        for tipo in tipos_esperados:
            assert tipo in tipos_choices


@pytest.mark.django_db
class TestRelacaoFamiliarAPI:
    """Testes da API de Relações Familiares."""
    
    def test_listar_relacoes_familiares(self, api_client, membro_origem, membro_destino):
        """Testa listagem de relações familiares."""
        RelacaoFamiliar.objects.create(
            membro_origem=membro_origem,
            membro_destino=membro_destino,
            tipo_relacao='pai'
        )
        
        url = reverse('relacoesfamiliares:relacaofamiliar-list')
        response = api_client.get(url)
        
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) >= 1
    
    def test_criar_relacao_familiar_api(self, api_client, relacao_data):
        """Testa criação de relação via API."""
        url = reverse('relacoesfamiliares:relacaofamiliar-list')
        response = api_client.post(url, relacao_data, format='json')
        
        assert response.status_code == status.HTTP_201_CREATED
        assert RelacaoFamiliar.objects.count() == 1
        assert response.data['tipo_relacao'] == 'pai'
    
    def test_validacao_relacao_mesma_pessoa(self, api_client, membro_origem):
        """Testa validação de relação de um membro consigo mesmo."""
        url = reverse('relacoesfamiliares:relacaofamiliar-list')
        data = {
            'membro_origem': membro_origem.id,
            'membro_destino': membro_origem.id,
            'tipo_relacao': 'pai'
        }
        
        response = api_client.post(url, data, format='json')
        
        assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    def test_filtrar_por_tipo_relacao(self, api_client, membro_origem, membro_destino):
        """Testa filtragem por tipo de relação."""
        RelacaoFamiliar.objects.create(
            membro_origem=membro_origem,
            membro_destino=membro_destino,
            tipo_relacao='pai'
        )
        
        url = reverse('relacoesfamiliares:relacaofamiliar-list')
        response = api_client.get(url, {'tipo_relacao': 'pai'})
        
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) >= 1
        assert all(r['tipo_relacao'] == 'pai' for r in response.data)
