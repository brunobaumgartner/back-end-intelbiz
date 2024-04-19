from sqlalchemy import Column, Integer, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from model.base import Base
from model.produto import Produto
from model.cliente import Cliente

class Venda(Base):
    __tablename__ = 'vendas'

    id = Column(Integer, primary_key = True)
    venda_id = Column(Integer)
    produto_id = Column(Integer, ForeignKey("produtos.id"))
    cliente_id = Column(Integer, ForeignKey("clientes.id")) 
    quantidade = Column(Integer)
    valor = Column(Float)
    data_venda = Column(DateTime, default = datetime.now())

    cliente = relationship("Cliente", back_populates="vendas")
    produto = relationship("Produto", back_populates="vendas")

    def __init__(self, venda:int, produto:int, cliente:int, 
                 quantidade:int, valor:float):
        self.venda_id = venda
        self.produto_id = produto
        self.cliente_id = cliente
        self.quantidade = quantidade
        self.valor = valor