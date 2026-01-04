from sqlalchemy import Column, Integer, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from src.database.base import Base

class ItemEmprestimo(Base):
    __tablename__ = "item_emprestimo"
    id_emprestimo = Column(Integer, ForeignKey("emprestimo.id_emprestimo"), primary_key=True)
    id_livro = Column(Integer, ForeignKey("livro.id_livro"), primary_key=True)
    data_prev_entrega = Column(DateTime, nullable=False)
    data_devolucao = Column(DateTime, nullable=False)

    # Relações: A entidade 'item_emprestimo' tem relação direta com as entidades 'livro' e 'empréstimo'

    emprestimo = relationship("Emprestimo", back_populates="itens")    
    livros = relationship("Livro", back_populates="itens")

    __table_args__ = (UniqueConstraint(
        "id_emprestimo", "id_livro", name = "uq_item_emprestimo"),)
    
