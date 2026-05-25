"""
Teste manual de CRUD para Emprestimo e ItemEmprestimo.

Este teste cria dados auxiliares:
1. Usuario
2. Funcionario
3. Livro

Depois cria:
4. Emprestimo
5. ItemEmprestimo

Ao final, remove o emprestimo. Como o relacionamento usa cascade,
o ItemEmprestimo deve ser removido junto.
"""

from pathlib import Path
import sys
import logging
from datetime import date, datetime, timedelta, timezone

ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT_DIR))

LOG_DIR = ROOT_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_DIR / "crud_emprestimo_test.log", encoding="utf-8"),
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


def criar_dados_base(session):
    logger.info("Criando dados base para emprestimo")

    usuario = Usuario(
        nome="Usuario Emprestimo Teste",
        matricula="USRTESTEMP",
        email="usuario.emprestimo@email.com",
        telefone="11911110000",
        endereco="Rua Emprestimo, 100",
    )

    funcionario = Funcionario(
        nome="Funcionario Emprestimo Teste",
        cpf="22233344455",
        telefone="11922220000",
        email="funcionario.emprestimo@email.com",
        cargo="Atendente",
    )

    livro = Livro(
        titulo="Livro Emprestimo Teste",
        editora="Editora Emprestimo",
        ano_publicacao=date(2026, 1, 1),
        quantidade_estoque=3,
    )

    session.add_all([usuario, funcionario, livro])
    session.commit()

    session.refresh(usuario)
    session.refresh(funcionario)
    session.refresh(livro)

    logger.info("Usuario criado com ID: %s", usuario.id_usuario)
    logger.info("Funcionario criado com ID: %s", funcionario.id_funcionario)
    logger.info("Livro criado com ID: %s", livro.id_livro)

    return usuario, funcionario, livro


def testar_crud_emprestimo(session):
    logger.info("Iniciando CRUD de Emprestimo com ItemEmprestimo")

    usuario, funcionario, livro = criar_dados_base(session)

    emprestimo = Emprestimo(
        usuario=usuario,
        funcionario=funcionario,
    )

    item = ItemEmprestimo(
        livro=livro,
        data_prev_entrega=datetime.now(timezone.utc) + timedelta(days=7),
        data_devolucao=datetime.now(timezone.utc) + timedelta(days=10),
    )

    emprestimo.itens.append(item)

    session.add(emprestimo)
    session.commit()
    session.refresh(emprestimo)

    logger.info("Emprestimo criado com ID: %s", emprestimo.id_emprestimo)

    emprestimo_encontrado = session.scalar(
        select(Emprestimo).where(
            Emprestimo.id_emprestimo == emprestimo.id_emprestimo
        )
    )

    logger.info("Emprestimo encontrado com ID: %s", emprestimo_encontrado.id_emprestimo)
    logger.info("Usuario do emprestimo: %s", emprestimo_encontrado.usuario.nome)
    logger.info("Funcionario do emprestimo: %s", emprestimo_encontrado.funcionario.nome)
    logger.info("Quantidade de itens: %s", len(emprestimo_encontrado.itens))
    logger.info("Livro emprestado: %s", emprestimo_encontrado.itens[0].livro.titulo)

    emprestimo_encontrado.itens[0].data_devolucao = datetime.now(timezone.utc)
    session.commit()

    logger.info("ItemEmprestimo atualizado com data de devolucao")

    id_emprestimo = emprestimo_encontrado.id_emprestimo
    id_livro = livro.id_livro
    id_usuario = usuario.id_usuario
    id_funcionario = funcionario.id_funcionario

    session.delete(emprestimo_encontrado)
    session.commit()

    logger.info("Emprestimo removido com sucesso")

    item_removido = session.get(
        ItemEmprestimo,
        {
            "id_emprestimo": id_emprestimo,
            "id_livro": id_livro,
        },
    )

    if item_removido is None:
        logger.info("ItemEmprestimo removido automaticamente pelo cascade")
    else:
        logger.warning("ItemEmprestimo ainda existe apos remover Emprestimo")

    usuario_base = session.get(Usuario, id_usuario)
    funcionario_base = session.get(Funcionario, id_funcionario)
    livro_base = session.get(Livro, id_livro)

    session.delete(usuario_base)
    session.delete(funcionario_base)
    session.delete(livro_base)
    session.commit()

    logger.info("Dados base removidos com sucesso")


session = SessionLocal()

try:
    logger.info("Iniciando teste manual de Emprestimo")
    testar_crud_emprestimo(session)
    logger.info("Teste manual de Emprestimo finalizado com sucesso")

except Exception:
    session.rollback()
    logger.exception("ERRO no teste manual de Emprestimo")

finally:
    session.close()
    logger.info("Sessao encerrada")