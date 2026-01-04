
from src.database.connection import engine
# Importa o engine do SQLAlchemy, que representa a conexão com o banco (SQLite, DuckDB, etc).
# É ele que sabe onde está o banco (sqlite:///biblioteca.db, por exemplo).
# Sem isso o SQLAlchemy não tem como executar comandos SQL.
from src.database.base import Base
# A Base contém 'Base.metadata' e contêm todas as tabelas registradas na pasta 'models'
# Todos os 'models' DEVEM herdar dessa mesma Base.

# importa todos os models:
from src.models.usuario import Usuario
#from src.models.aluno import Aluno
#from src.models.professor import Professor
from src.models.livro import Livro
from src.models.emprestimo import Emprestimo
from src.models.item_emprestimo import ItemEmprestimo
from src.models.funcionario import Funcionario

Base.metadata.create_all(engine)
