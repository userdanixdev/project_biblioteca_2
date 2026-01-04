from sqlalchemy import Column, Integer, Date, VARCHAR
from sqlalchemy.orm import relationship
from src.database.base import Base

class Livro(Base):
    __tablename__ = "livro"
    id_livro = Column(Integer, primary_key=True)
    titulo = Column(VARCHAR(50), nullable=False)
    editora = Column(VARCHAR(50))
    ano_publicacao = Column(Date)
    quantidade_estoque = Column(Integer, nullable=False)

    # Relação: A entidade 'livro' se relaciona diretamente com a entidade 'item_emprestimo'

    itens = relationship("ItemEmprestimo", back_populates="livro")
    
