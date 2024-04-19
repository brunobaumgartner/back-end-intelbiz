from pydantic import BaseModel
from typing import Optional, List
from model.venda import Venda
from model.produto import Produto

class VendaSchema(BaseModel):
    """ Define como uma nova venda a ser inserida deve ser representado
    """
    venda_id: int = 1
    produto_id: int = 1
    cliente_id: int = 1
    quantidade: int = 1


class VendaBuscaSchema(BaseModel):
    """ Define os atributos que serão usados para realizar a busca de uma venda """
    cliente_id: int

class ListaVendasSchema(BaseModel):
    """ Define a lista de produtos será retornada. """
    vendas:List[VendaSchema]

class VendaViewSchema(BaseModel):
    """ Define como uma venda será retornada. """
    venda_id: int
    nome: str
    quantidade: int
    valor: float
    data_venda: str

def apresenta_vendas(vendas):
    """ Retorna uma representação das vendas seguindo o schema definido em VendaViewSchema. """
    result = []
    for venda in vendas:
        result.append({
            "venda_id": venda.venda_id,
            "nome": venda.nome, 
            "quantidade": venda.quantidade,
            "valor": venda.valor,
            "data_venda": venda.data_venda
        })

    return {"vendas": result}

def apresenta_venda(venda: Venda):
    """ Retorna uma representação da venda seguindo o schema definido em VendaViewSchema. """
    return {
        "venda_id": venda.venda_id,
        "produto_id": venda.produto_id,
        "cliente_id": venda.cliente_id,
        "quantidade": venda.quantidade,
        "valor": venda.valor,
    }

def apresenta_ultima_venda(venda: Venda):
    """ Retorna o ultimo id de venda"""
    return {
        "venda_ultimo_id": venda.venda_id
    }

class VendaDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição de remoção. """
    venda_id: int
    produto_id: int
    cliente_id: int
    quantidade: int
    valor: float

class ListagemVendasSchema(BaseModel):
    """ Define como uma listagem de produtos será retornada. """
    produtos:List[VendaSchema]