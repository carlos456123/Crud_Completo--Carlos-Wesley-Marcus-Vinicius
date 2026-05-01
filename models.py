from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from database import engine

Base = declarative_base()

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    categoria = Column(String, nullable=False)
    quantidade = Column(Integer, nullable=False)

Base.metadata.create_all(bind=engine)