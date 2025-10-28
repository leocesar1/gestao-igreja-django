# Sistema de Gestão de Igrejas - Django 5

Sistema completo de gestão para igrejas locais desenvolvido em Django 5, com arquitetura modularizada, REST API e suporte a Docker.

## 📋 Visão Geral

### Objetivo
Sistema destinado a igrejas locais para controle de:
- Membros e visitantes
- Famílias e relações familiares
- Usuários e permissões
- Base para módulos futuros: eventos, finanças, ministérios

### Stack Tecnológica
- **Backend**: Django 5.0
- **API**: Django REST Framework 3.14
- **Banco de Dados**: PostgreSQL 16
- **Autenticação**: Custom User Model com UUID
- **Testes**: Pytest + pytest-django
- **Deploy**: Docker + Docker Compose
- **Internacionalização**: pt-BR

## 🚀 Início Rápido

### 1. Clonar o repositório
```bash
git clone https://github.com/leocesar1/gestao-igreja-django.git
cd gestao-igreja-django
```

### 2. Criar ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente
```bash
cp .env.example .env
```

### 5. Executar com Docker
```bash
docker-compose up -d
```

### 6. Aplicar migrações
```bash
docker-compose exec web python manage.py migrate
```

### 7. Criar superusuário
```bash
docker-compose exec web python manage.py createsuperuser
```

### 8. Criar categorias de usuários (opcional)
```bash
docker-compose exec web python manage.py criarcategorias
```

## 📦 Estrutura do Projeto

```
gestaoigreja/
├── manage.py
├── requirements.txt
├── docker-compose.yml
├── .env.example
├── pytest.ini
├── README.md
├── gestaoigreja/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── pessoas/        # Modelo base de pessoas
├── membros/        # Membros da igreja
├── visitantes/     # Visitantes
├── familias/       # Famílias
├── relacoesfamiliares/  # Relações entre membros
└── usuarios/       # Autenticação customizada
```

## 🧪 Testes

### Executar todos os testes
```bash
docker-compose exec web pytest
```

### Executar com cobertura
```bash
docker-compose exec web pytest --cov
```

## 🔗 API Endpoints

### Pessoas
- `GET /api/pessoas/` - Listar pessoas
- `POST /api/pessoas/` - Criar pessoa
- `GET /api/pessoas/{id}/` - Detalhes
- `PUT /api/pessoas/{id}/` - Atualizar
- `DELETE /api/pessoas/{id}/` - Remover

### Membros
- `GET /api/membros/` - Listar membros
- `POST /api/membros/` - Criar membro
- `GET /api/membros/{id}/` - Detalhes
- `PUT /api/membros/{id}/` - Atualizar
- `DELETE /api/membros/{id}/` - Remover

### Visitantes
- `GET /api/visitantes/` - Listar visitantes
- `POST /api/visitantes/` - Criar visitante
- `GET /api/visitantes/{id}/` - Detalhes
- `PUT /api/visitantes/{id}/` - Atualizar
- `DELETE /api/visitantes/{id}/` - Remover

### Famílias
- `GET /api/familias/` - Listar famílias
- `POST /api/familias/` - Criar família
- `GET /api/familias/{id}/` - Detalhes
- `PUT /api/familias/{id}/` - Atualizar
- `DELETE /api/familias/{id}/` - Remover

### Relações Familiares
- `GET /api/relacoes-familiares/` - Listar relações
- `POST /api/relacoes-familiares/` - Criar relação
- `GET /api/relacoes-familiares/{id}/` - Detalhes
- `PUT /api/relacoes-familiares/{id}/` - Atualizar
- `DELETE /api/relacoes-familiares/{id}/` - Remover

### Usuários
- `GET /api/usuarios/` - Listar usuários
- `POST /api/usuarios/` - Criar usuário
- `GET /api/usuarios/{id}/` - Detalhes
- `PUT /api/usuarios/{id}/` - Atualizar
- `DELETE /api/usuarios/{id}/` - Remover

## 📚 Módulos do Sistema

### 1. Pessoas
Modelo base com informações pessoais compartilhadas.

### 2. Membros
Extensão de Pessoa com dados eclesísticos (batismo, admissão, cargo, etc).

### 3. Visitantes
Controle de visitantes com informações de primeira visita e acompanhamento.

### 4. Famílias
Agrupamento de membros em núcleos familiares.

### 5. Relações Familiares
Vínculos entre membros (pai/mãe, filho/filha, cônjuge, etc).

### 6. Usuários
Autenticação customizada com categorias e permissões específicas.

## 🔒 Categorias de Usuário

- **Pastor**: Acesso total ao sistema
- **Secretaria**: Gerencia cadastros e eventos
- **Tesouraria**: Gerencia finanças

## 🛠️ Próximos Módulos

- [ ] Doações/Finanças
- [ ] Eventos
- [ ] Ministérios
- [ ] Células
- [ ] Patrimônio
- [ ] Comunicação

## 📖 Documentação

- [Django Documentation](https://docs.djangoproject.com)
- [Django REST Framework](https://www.django-rest-framework.org)
- [PostgreSQL](https://www.postgresql.org/docs)
- [Docker](https://docs.docker.com)

## 📝 Licença

MIT

## 👥 Autor

Sistema Gestão de Igrejas

---

**Versão**: 1.0.0  
**Data**: Outubro 2025
