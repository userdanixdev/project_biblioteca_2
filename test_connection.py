"""
Arquivo: test_conexao.py

Objetivo:
    Validar a conexão inicial do projeto com o banco de dados oficial:
    project_biblioteca.db.

Contexto da evolução do projeto:
    Este arquivo marca o início da fase de evolução prática do sistema de
    biblioteca. Até aqui, o projeto concentrou-se na modelagem de dados,
    organização dos models ORM e criação da estrutura do banco.

    A partir desta etapa, o foco passa a ser validar o funcionamento real da
    aplicação por camadas:

    1. Conexão com o banco de dados
    2. Testes manuais de CRUD
    3. Testes automatizados com logs
    4. Criação da API
    5. Desenvolvimento da interface web

Por que começar pela conexão:
    Antes de inserir, consultar, atualizar ou remover dados, é necessário
    confirmar que o SQLAlchemy consegue abrir uma conexão com o banco correto
    e que as tabelas esperadas existem.

Banco oficial do projeto:
    O banco adotado como fonte principal do sistema é:

        project_biblioteca.db

Observação:
    Este arquivo é apenas um teste inicial de conexão. Ele não deve alterar
    dados no banco. Seu papel é verificar se a aplicação consegue enxergar
    corretamente a estrutura já criada.
"""

from sqlalchemy import text
from src.database.connection import engine

with engine.connect() as connection:
    result = connection.execute(text("SELECT name FROM sqlite_master WHERE type='table';"))
    tables = result.fetchall()

print("Conexao OK")
print("Tabelas encontradas:")
for table in tables:
    print("-", table[0])