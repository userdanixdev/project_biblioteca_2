from flask import Flask
from src.config import Config
from src.extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config) # Carrega as configurações do banco.
    db.init_app(app)  # Conecta o Flask-SQLAlchemy à aplicação.
    migrate.init_app(app,db)  #Conecta o Flask-Migrate à aplicação e à metadata dos models.

# Importa seus models dentro do contexto Flask,
# garantindo que o SQLAlchemy conheça todas as tabelas antes do Alembic tentar gerar migrations.
    with app.app_context():
        importar_models()

# Cria uma rota simples para testar se a aplicação, persistência.
    @app.get("/initial")        
    def initial_check():
        return {"status":"ok"}
    
    return app

def importar_models():
    from src.models.usuario import Usuario, Aluno, Professor
    from src.models.funcionario import Funcionario
    from src.models.livro import Livro
    from src.models.emprestimo import Emprestimo
    from src.models.item_emprestimo import ItemEmprestimo

    return (
        Usuario,
        Aluno,
        Professor,
        Funcionario,
        Livro,
        Emprestimo,
        ItemEmprestimo,
    )