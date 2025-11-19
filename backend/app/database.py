from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./petshop.db"

engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}  # necessário pro SQLite funcionar
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    # cria as tabelas no banco
    Base.metadata.create_all(bind=engine)

