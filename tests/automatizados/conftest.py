import logging

# Importa o pytest, framework responsavel por executar os testes.
# Tambem usamos pytest.fixture para criar recursos reutilizaveis nos testes.
import pytest

# Importa create_engine para criar uma conexao com o banco de teste.
# Importa event para configurar comportamentos extras no engine,
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker

from src.database.base import Base

from src.models.usuario import Usuario, Aluno, Professor
from src.models.funcionario import Funcionario
from src.models.livro import Livro
from src.models.emprestimo import Emprestimo
from src.models.item_emprestimo import ItemEmprestimo


logger = logging.getLogger(__name__)


# Registra um evento que sera executado sempre que o engine abrir conexao.
# No SQLite, foreign keys precisam ser ativadas manualmente.
@pytest.fixture()
def engine():
    logger.info("Criando banco SQLite em memoria para teste")

    test_engine = create_engine("sqlite:///:memory:", future=True)

    @event.listens_for(test_engine, "connect")
    def enable_foreign_keys(dbapi_connection, connection_record):
        cursor = dbapi_connection.cursor()
        # Ativa a validacao de chaves estrangeiras no SQLite.
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()

# Cria no banco em memoria todas as tabelas definidas nos models.
# Isso usa o metadata da Base, alimentado pelos imports dos models acima.        
    Base.metadata.create_all(test_engine)

    yield test_engine

    Base.metadata.drop_all(test_engine)
    logger.info("Banco SQLite em memoria removido")

# Define uma fixture chamada session.
# Ela depende da fixture engine, por isso recebe engine como parametro.
# Sempre que um teste pedir session, o pytest cria primeiro o engine.
@pytest.fixture()
def session(engine):
    # Cria uma fabrica de sessoes vinculada ao engine de teste.
    # Cada sessao criada por ela conversa com o banco SQLite em memoria.
    SessionTesting = sessionmaker(bind=engine, future=True)

    db = SessionTesting()
    logger.info("Sessao de teste aberta")

    try:
        yield db
    finally:
        db.close()
        logger.info("Sessao de teste fechada")

# O conftest.py serve para preparar recursos reutilizáveis dos testes.
# Neste caso, ele cria um banco SQLite temporário em memória e uma sessão SQLAlchemy 
# limpa para cada teste. Assim seus testes automatizados não mexem no project_biblioteca.db.        