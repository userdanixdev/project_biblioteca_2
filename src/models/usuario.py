from sqlalchemy import Column, Integer, VARCHAR, CHAR, ForeignKey
from sqlalchemy.orm import relationship
from src.database.base import Base

class Usuario(Base):
    __tablename__ =  "usuario"
    id_usuario = Column(Integer, primary_key=True)
    nome = Column(VARCHAR(50), nullable=False)
    matricula = Column(CHAR(10),unique=True)
    email = Column(VARCHAR(20), nullable=False)
    telefone = Column(VARCHAR(15), nullable=False)
    endereco = Column(VARCHAR(50), nullable=False)

    # Relação: A entidade 'usuario' tem relação direta com a entidade 'emprestimo':
    emprestimos = relationship("Emprestimo", back_populates="usuario")

    __mapper_args__= {"polymorphic_identity": "usuario", "polymorphic_on": None}
# Especialização:
class Aluno(Usuario):
    __tablename__= "aluno"
    id_usuario = Column(Integer, ForeignKey("usuario.id_usuario"), primary_key=True)  
    __mapper_args__={"polymorphic_identity":"aluno",} 
# Especialização:
class Professor(Usuario):
    __tablename__= "professor"
    id_usuario=Column(Integer, ForeignKey("usuario.id_usuario"),primary_key=True)    

    __mapper_args__={"polymorphic_identity":"professor",}          

