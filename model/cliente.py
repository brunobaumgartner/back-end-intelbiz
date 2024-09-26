from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.orm import relationship
from datetime import datetime
from model.base import Base

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key = True)
    nome = Column(String(140))
    endereco = Column(String(150))
    telefone = Column(Integer, unique=True)
    data_insercao = Column(DateTime, default = datetime.now())

    
    vendas = relationship("Venda", back_populates="cliente")

    def __init__(self, nome:str,  endereco:str, telefone:int):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone