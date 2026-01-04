
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from src.database.base import Base

# Representa o ato administrativo do empréstimo:
class Emprestimo(Base):
    __tablename__ = "emprestimo"

    id_emprestimo = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    id_funcionario = Column(Integer, ForeignKey("funcionario.id_funcionario"), nullable=False)
    data_emprestimo = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # Relacionamentos: A entidade se relaciona diretamente com 'item_emprestimo','funcionario','usuario':
    funcionario = relationship("Funcionario", back_populates="emprestimo")
    usuario = relationship("Usuario", back_populates="emprestimo")
    itens = relationship(
        "ItemEmprestimo",
        back_populates="emprestimo",
        cascade="all, delete-orphan"
    )
