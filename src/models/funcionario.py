from sqlalchemy import Column, Integer, VARCHAR, CHAR
from sqlalchemy.orm import relationship
from src.database.base import Base

class Funcionario(Base):
    __tablename__ = "funcionario"
    id_funcionario = Column(Integer,primary_key=True)
    nome = Column(CHAR(50),nullable=False)
    cpf= Column(VARCHAR(15),unique=True, nullable=False)
    telefone = Column(VARCHAR(50),unique=True,nullable=False)
    email = Column(VARCHAR(50),nullable=False)
    cargo = Column(CHAR(15),nullable=False)

    # Relacionamentos: A entidade 'funcionario' se relaciona com 'empréstimo' diretamente:

    emprestimo =relationship ("Emprestimo", back_populates= "funcionario")