from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from src.database.base import Base

db = SQLAlchemy(model_class=Base)
migrate = Migrate(compare_type=True, render_as_batch=True)

## O parâmetro 'compare_type' manda o Alembic comparar também os tipos das colunas.
# Exemplo: se hoje seu model tem:

# nome = Column(VARCHAR(50))
# E amanhã você mudar para:
# nome = Column(VARCHAR(100))
# Com compare_type=True, o Alembic consegue perceber essa mudança e gerar uma migration.
# Sem isso, algumas alterações de tipo poderiam passar despercebidas.

## O 'render_as_batch=True' É especialmente importante com SQLite. O SQLite tem limitações
# para alterar tabelas diretamente. Por exemplo, algumas operações de ALTER TABLE
#  não funcionam como em PostgreSQL ou MySQL.
# Com render_as_batch=True, o Alembic usa uma estratégia mais segura para SQLite:
# 1. cria uma tabela temporária com a nova estrutura
# 2. copia os dados da tabela antiga
# 3. remove a tabela antiga
# 4. renomeia a tabela nova
## Isso é chamado de batch mode.
# Em resumo: é uma maneira de deixar o Migrate mais seguro compatíveis com SQlite
