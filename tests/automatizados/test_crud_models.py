import logging
from datetime import date, datetime, timedelta, timezone

from sqlalchemy import inspect, select
from sqlalchemy.orm import configure_mappers

# configure_mappers força o SQLAlchemy a configurar todos os mapeamentos ORM naquele momento.

# inspect serve para inspecionar objetos do SQLAlchemy. No seu teste, usamos para olhar o banco
#  criado em memória e verificar quais tabelas existem.

from src.models.usuario import Usuario
from src.models.funcionario import Funcionario
from src.models.livro import Livro
from src.models.emprestimo import Emprestimo
from src.models.item_emprestimo import ItemEmprestimo


logger = logging.getLogger(__name__)

# Valida se o SQLAlchemy consegue configurar todos os relacionamentos dos models.
# Se tiver back_populates errado ou classe não importada, esse teste falha.

def test_mapeamento_orm_configura_sem_erros():
    logger.info("Validando mapeamento ORM")

    configure_mappers()
# Se o ORM estiver inconsistente, esse teste falha logo no início.
# Se passar, os relacionamentos básicos foram reconhecidos pelo SQLAlchemy.

# Usa o engine criado pelo conftest.py e verifica se as tabelas foram criadas:
def test_cria_tabelas_esperadas(engine):
    logger.info("Validando tabelas criadas")

    tabelas = set(inspect(engine).get_table_names())
# ele pergunta ao banco “quais tabelas você tem?”. Isso permite testar se:
#  usuario, livro, emprestimo etc. foram criadas corretamente.    

    assert "usuario" in tabelas
    assert "aluno" in tabelas
    assert "professor" in tabelas
    assert "funcionario" in tabelas
    assert "livro" in tabelas
    assert "emprestimo" in tabelas
    assert "item_emprestimo" in tabelas


def test_crud_livro(session):
    logger.info("Testando CRUD de Livro")

    livro = Livro(
        titulo="Livro Pytest",
        editora="Editora Pytest",
        ano_publicacao=date(2026, 1, 1),
        quantidade_estoque=5,
    )

    session.add(livro)
    session.commit()
    session.refresh(livro)

    assert livro.id_livro is not None

    livro_encontrado = session.scalar(
        select(Livro).where(Livro.id_livro == livro.id_livro)
    )

    assert livro_encontrado is not None
    assert livro_encontrado.titulo == "Livro Pytest"

    livro_encontrado.quantidade_estoque = 10
    session.commit()
    session.refresh(livro_encontrado)

    assert livro_encontrado.quantidade_estoque == 10

    session.delete(livro_encontrado)
    session.commit()

    assert session.get(Livro, livro.id_livro) is None


def test_crud_usuario(session):
    logger.info("Testando CRUD de Usuario")

    usuario = Usuario(
        nome="Usuario Pytest",
        matricula="USRTESTPY",
        email="usuario.pytest@email.com",
        telefone="11999990000",
        endereco="Rua Pytest, 123",
    )

    session.add(usuario)
    session.commit()
    session.refresh(usuario)

    assert usuario.id_usuario is not None

    usuario_encontrado = session.scalar(
        select(Usuario).where(Usuario.id_usuario == usuario.id_usuario)
    )

    assert usuario_encontrado is not None
    assert usuario_encontrado.nome == "Usuario Pytest"

    usuario_encontrado.telefone = "11888880000"
    session.commit()
    session.refresh(usuario_encontrado)

    assert usuario_encontrado.telefone == "11888880000"

    session.delete(usuario_encontrado)
    session.commit()

    assert session.get(Usuario, usuario.id_usuario) is None


def test_crud_funcionario(session):
    logger.info("Testando CRUD de Funcionario")

    funcionario = Funcionario(
        nome="Funcionario Pytest",
        cpf="12345678901",
        telefone="11777770000",
        email="funcionario.pytest@email.com",
        cargo="Atendente",
    )

    session.add(funcionario)
    session.commit()
    session.refresh(funcionario)

    assert funcionario.id_funcionario is not None

    funcionario_encontrado = session.scalar(
        select(Funcionario).where(
            Funcionario.id_funcionario == funcionario.id_funcionario
        )
    )

    assert funcionario_encontrado is not None
    assert funcionario_encontrado.nome == "Funcionario Pytest"

    funcionario_encontrado.cargo = "Bibliotecario"
    session.commit()
    session.refresh(funcionario_encontrado)

    assert funcionario_encontrado.cargo == "Bibliotecario"

    session.delete(funcionario_encontrado)
    session.commit()

    assert session.get(Funcionario, funcionario.id_funcionario) is None


def test_cria_emprestimo_com_item(session):
    logger.info("Testando Emprestimo com ItemEmprestimo")

    usuario = Usuario(
        nome="Usuario Emprestimo Pytest",
        matricula="USREMPPY",
        email="usuario.emp.pytest@email.com",
        telefone="11911110000",
        endereco="Rua Emprestimo Pytest, 1",
    )

    funcionario = Funcionario(
        nome="Funcionario Emprestimo Pytest",
        cpf="22233344455",
        telefone="11922220000",
        email="funcionario.emp.pytest@email.com",
        cargo="Atendente",
    )

    livro = Livro(
        titulo="Livro Emprestimo Pytest",
        editora="Editora Pytest",
        ano_publicacao=date(2026, 1, 1),
        quantidade_estoque=3,
    )

    session.add_all([usuario, funcionario, livro])
    session.commit()

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

    emprestimo_encontrado = session.get(Emprestimo, emprestimo.id_emprestimo)

    assert emprestimo_encontrado is not None
    assert emprestimo_encontrado.usuario.nome == "Usuario Emprestimo Pytest"
    assert emprestimo_encontrado.funcionario.nome == "Funcionario Emprestimo Pytest"
    assert len(emprestimo_encontrado.itens) == 1
    assert emprestimo_encontrado.itens[0].livro.titulo == "Livro Emprestimo Pytest"