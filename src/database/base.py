from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

# Uma única fonte de verdade e evita erro de múltiplas bases.

