#!/usr/bin/env python
"""Script de gerenciamento do Django para tarefas administrativas."""
import os
import sys


def main():
    """Executa tarefas administrativas."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestaoigreja.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Não foi possível importar o Django. Você tem certeza de que está "
            "instalado e disponível na variável de ambiente PYTHONPATH? "
            "Você esqueceu de ativar o ambiente virtual?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
