from sqlalchemy import Column, Integer, DateTime, Float, String
from datetime import datetime
from sqlalchemy.orm import relationship
from model.base import Base

class Produto(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key = True)
    nome = Column(String(300), unique=True)
    quantidade = Column(Integer)
    valor = Column(Float)
    data_insercao = Column(DateTime, default = datetime.now())
    
    vendas = relationship("Venda", back_populates="produto")

    def __init__(self, nome:str, quantidade:int, valor:float):
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor