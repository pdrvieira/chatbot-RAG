from sqlalchemy import Column, Integer, String, Text
from .database import Base


class Document(Base):
    __tablename__ = "documentos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True, nullable=False)
    conteudo = Column(Text, nullable=False)
    embedding = Column(Text, nullable=False)  # salvo como JSON string

