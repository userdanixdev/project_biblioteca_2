"""
Teste manual de CRUD usando o banco oficial project_biblioteca.db.

Este arquivo valida:
1. CRUD de Livro
2. CRUD de Usuario
3. CRUD de Funcionario

Observacao:
    Este arquivo altera dados temporariamente no banco, mas remove ao final
    os registros criados durante o teste.
"""

from pathlib import Path
import sys
import logging
from datetime import date

ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT_DIR))

LOG_DIR = ROOT_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_DIR / "crud_test.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)

from sqlalchemy import select

from src.database.connection import SessionLocal
from src.models.usuario import Usuario, Aluno, Professor
from src.models.funcionario import Funcionario
from src.models.emprestimo import Emprestimo
from src.models.item_emprestimo import ItemEmprestimo
from src.models.livro import Livro


def testar_crud_livro(session):
    logger.info("Iniciando CRUD de Livro")

    livro = Livro(
        titulo="Livro Teste Manual",
        editora="Editora Teste",
        ano_publicacao=date(2026, 1, 1),
        quantidade_estoque=5,
    )

    session.add(livro)
    session.commit()
    session.refresh(livro)

    logger.info("Livro criado com ID: %s", livro.id_livro)

    livro_encontrado = session.scalar(
        select(Livro).where(Livro.id_livro == livro.id_livro)
    )

    logger.info("Livro encontrado: %s", livro_encontrado.titulo)

    livro_encontrado.quantidade_estoque = 10
    session.commit()
    session.refresh(livro_encontrado)

    logger.info("Livro atualizado. Novo estoque: %s", livro_encontrado.quantidade_estoque)

    session.delete(livro_encontrado)
    session.commit()

    logger.info("Livro removido com sucesso")


def testar_crud_usuario(session):
    logger.info("Iniciando CRUD de Usuario")

    usuario = Usuario(
        nome="Usuario Teste Manual",
        matricula="USRTEST001",
        email="usuario.teste@email.com",
        telefone="11999990000",
        endereco="Rua Teste, 123",
    )

    session.add(usuario)
    session.commit()
    session.refresh(usuario)

    logger.info("Usuario criado com ID: %s", usuario.id_usuario)

    usuario_encontrado = session.scalar(
        select(Usuario).where(Usuario.id_usuario == usuario.id_usuario)
    )

    logger.info("Usuario encontrado: %s", usuario_encontrado.nome)

    usuario_encontrado.telefone = "11888880000"
    session.commit()
    session.refresh(usuario_encontrado)

    logger.info("Usuario atualizado. Novo telefone: %s", usuario_encontrado.telefone)

    session.delete(usuario_encontrado)
    session.commit()

    logger.info("Usuario removido com sucesso")


def testar_crud_funcionario(session):
    logger.info("Iniciando CRUD de Funcionario")

    funcionario = Funcionario(
        nome="Funcionario Teste Manual",
        cpf="12345678901",
        telefone="11777770000",
        email="funcionario.teste@email.com",
        cargo="Atendente",
    )

    session.add(funcionario)
    session.commit()
    session.refresh(funcionario)

    logger.info("Funcionario criado com ID: %s", funcionario.id_funcionario)

    funcionario_encontrado = session.scalar(
        select(Funcionario).where(Funcionario.id_funcionario == funcionario.id_funcionario)
    )

    logger.info("Funcionario encontrado: %s", funcionario_encontrado.nome)

    funcionario_encontrado.cargo = "Bibliotecario"
    session.commit()
    session.refresh(funcionario_encontrado)

    logger.info("Funcionario atualizado. Novo cargo: %s", funcionario_encontrado.cargo)

    session.delete(funcionario_encontrado)
    session.commit()

    logger.info("Funcionario removido com sucesso")


session = SessionLocal()

try:
    logger.info("Iniciando testes manuais de CRUD")

    testar_crud_livro(session)
    testar_crud_usuario(session)
    testar_crud_funcionario(session)

    logger.info("Todos os testes manuais de CRUD finalizaram com sucesso")

except Exception:
    session.rollback()
    logger.exception("ERRO nos testes manuais de CRUD")

finally:
    session.close()
    logger.info("Sessao encerrada")