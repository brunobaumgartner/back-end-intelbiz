from pydantic import BaseModel
from typing import List
from model.cliente import Cliente

class ClienteSchema(BaseModel):
    """ Define como um novo cliente a ser inserido deve ser representado
    """
    nome: str = "Rogerio"
    endereco: str = "Rua batata, 543"
    telefone: int = 21999988888

class ClienteViewSchema(BaseModel):
    """ Define como um cliente será retornado: cliente + comentários.
    """
    id: int = 1
    nome: str = "Rogerio"
    endereco: str = "Rua batata, 543"
    telefone: int = 21999988888

class ClienteBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do cliente.
    """
    id: int = 1

def apresenta_cliente(cliente: Cliente):
    """ Retorna uma representação do cliente seguindo o schema definido em
        clienteViewSchema. """
    return {
        "nome": cliente.nome,
        "endereco": cliente.endereco,
        "telefone": cliente.telefone
    }

def apresenta_clientes(clientes: List[Cliente]):
    """ Retorna uma representação do cliente seguindo o schema definido em
        ClienteViewSchema.
    """
    result = []
    for cliente in clientes:
        result.append({
            "id": cliente.id,
            "nome": cliente.nome,
            "endereco": cliente.endereco,
            "telefone": cliente.telefone
        })

    return {"clientes": result}

class ClienteDelSchema(BaseModel):
    """ Define a estrutura de um cliente. """
    nome: str = "Rogerio"
    endereco: str = "Rua batata, 543"
    telefone: int = 21999988888

class ListaClientesSchema(BaseModel):
    """Define como será a lista de clientes"""
    clientes:List[ClienteSchema]

class ClienteUpdateSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do cliente.
    """
    nome: str
    email: str
    telefone: int