from pathlib import Path


class Config:
    BASE_DIR = Path(__file__).resolve().parents[1]
    DATABASE_PATH = BASE_DIR / "project_biblioteca.db"

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DATABASE_PATH.as_posix()}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    # O SQLALCHEMY_TRACK_MODIFICATIONS desativado é um recurso antigo do
    #  Flask-SQLAlchemy que rastreava modificações em objetos para emitir sinais/eventos.
# Na prática consome memória; pode gerar warnings.
