from flask_openapi3 import OpenAPI, Tag
from flask import redirect
from urllib.parse import unquote
from logger import logger

from model import *
from schemas.cliente import *
from schemas.produto import *
from schemas.venda import *
from schemas.error import *

from flask_cors import CORS
app = OpenAPI(__name__)
CORS(app)

home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
cliente_tag = Tag(name="Cliente", description="Adição, visualização e remoção de clientes da base")
produto_tag = Tag(name="Produto", description="Adição, visualização e remoção de produtos da base")
venda_tag = Tag(name="Venda", description="Adição, visualização e remoção de vendas da base")

@app.get('/')
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

#CLIENTES

@app.get('/cliente', tags=[cliente_tag], 
         responses={"200": ListaClientesSchema, "404": ErrorSchema})
def get_clientes():
    """ Busca todos os clientes """
    logger.debug(f"Coletando clientes")
    try:
        session = Session()
        clientes = session.query(Cliente).all()
        session.close()
        if not clientes:
            return {"clientes": []}, 200
        else:
            return apresenta_clientes(clientes), 200
        
    except Exception as e:
        error_msg = "Não foi possivel encontrar clientes"
        logger.debug(f"Erro ao realizar a busca, {error_msg}")
        return {"mesage": error_msg, "Erro": e }, 400

@app.get('/cliente/', tags=[cliente_tag],
         responses={"200": ClienteViewSchema, "404": ErrorSchema})
def get_cliente(query: ClienteBuscaSchema):
    """Faz a busca por cliente cadastrado
    Retorna com o id fornecido.
    """
    logger.debug(f"Coletando cliente")
    try:
        session = Session()
        clientes = session.query(Cliente).filter(Cliente.id == query.id).all()

        if not clientes:
            return {"clientes": []}, 200
        else:
            return apresenta_clientes(clientes), 200
        
    except Exception as e:
        error_msg = "Não foi possivel encontrar clientes"
        logger.debug(f"Erro ao realizar a busca, {error_msg}")
        return {"mesage": error_msg, "Erro": e }, 400

@app.post('/cliente/', tags=[cliente_tag],
          responses={"200": ClienteViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def set_cliente(form: ClienteSchema):
    """Adiciona um novo Cliente à base de dados"""
    cliente = Cliente(
        nome = form.nome,
        endereco = form.endereco,
        telefone = form.telefone)
    try:
        session = Session()
        session.add(cliente)
        session.commit()
        logger.debug(f"Adicionado cliente de nome: '{cliente.nome}'")
        session.close()
        return apresenta_cliente(cliente), 200
    
    except Exception as e:
        error_msg = "Não foi possível salvar o novo cliente! "
        return {"mesage": error_msg}, 400

@app.delete('/cliente/', tags=[cliente_tag], 
            responses={"200": ClienteDelSchema, "404": ErrorSchema})
def del_cliente(query: ClienteBuscaSchema):
    """Deleta o cliente a partir do telefone"""
    logger.debug(f"Deletando cliente: {query.id}")
    try:
        session = Session()
        # fazendo a remoção
        count = session.query(Cliente).filter(Cliente.id == query.id).delete()
        session.commit()

        if count:
            logger.debug(f"Cliente deletado!")
            return {"mesage": "Cliente deletado"}
        else: 
            logger.warning(f"Erro ao deletar o cliente")
            return {"mesage": "Cliente não encontrado na base"}, 404
    except Exception as e:
        error_msg = "Não foi possivel deletar o clientes"
        logger.debug(f"Erro ao tentar deletar o cliente, {error_msg}")

        return {"mesage": error_msg, "Erro": e }, 400

#PRODUTOS

@app.post('/produto', tags=[produto_tag],
          responses={"200": ProdutoViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def set_produto(form: ProdutoSchema):
    """Adiciona um novo Produto à base de dados

    Retorna uma representação dos produtos.
    """
    produto = Produto(
        nome = form.nome,
        quantidade = form.quantidade,
        valor = form.valor)
    try:
        session = Session()
        session.add(produto)
        session.commit()
        logger.debug(f"Adicionado produto de nome: '{produto.nome}'")
        return apresenta_produto(produto), 200

    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        return {"mesage": error_msg}, 400
    
@app.get('/produto', tags=[produto_tag],
         responses={"200": ListagemProdutosSchema, "404": ErrorSchema})
def get_produtos():
    """Faz a busca por todos os Produto cadastrados."""
    logger.debug(f"Coletando produtos ")
    session = Session()
    produtos = session.query(Produto).all()

    if not produtos:
        return {"produtos": []}, 200
    else:
        logger.debug(f"%d rodutos econtrados" % len(produtos))
        print(produtos)
        return apresenta_produtos(produtos), 200

@app.get('/produto/', tags=[produto_tag],
         responses={"200": ProdutoViewSchema, "404": ErrorSchema})
def get_produto(query: ProdutoBuscaSchema):
    """Faz a busca por um Produto a partir do nome do produto
    Retorna uma representação dos produtos.
    """
    produto_nome = query.nome
    logger.debug(f"Coletando dados sobre produto #{produto_nome}")
    session = Session()
    produto = session.query(Produto).filter(Produto.nome == produto_nome).all()

    if not produto:
        error_msg = "Produto não encontrado na base :/"
        logger.warning(f"Erro ao buscar produto '{produto_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Produto econtrado: '{produto}'")
        return apresenta_produtos(produto), 200

@app.delete('/produto/', tags=[produto_tag],
            responses={"200": ProdutoDelSchema, "404": ErrorSchema})
def del_produto(query: ProdutoBuscaSchema):
    """Deleta um Produto a partir do nome de produto informado

    Retorna uma mensagem de confirmação da remoção.
    """
    produto_nome = unquote(unquote(query.nome))
    print(produto_nome)
    logger.debug(f"Deletando dados sobre produto #{produto_nome}")
    session = Session()
    count = session.query(Produto).filter(Produto.nome == produto_nome).delete()
    session.commit()

    if count:
        logger.debug(f"Deletado produto #{produto_nome}")
        return {"mesage": "Produto removido", "id": produto_nome}
    else:
        error_msg = "Produto não encontrado na base :/"
        logger.warning(f"Erro ao deletar produto #'{produto_nome}', {error_msg}")
        return {"mesage": error_msg}, 404

@app.put('/produto/', tags=[produto_tag],
            responses={"200": ClienteViewSchema, "404": ErrorSchema})
def update_produto(form: ProdutoUpdateSchema):
    """Atualiza o produto associado ao nome inserido"""
    session = Session()
    
    #Verifica a existencia do produto
    produto_nome = form.nome
    logger.debug(f"Verificando se o produto '{produto_nome}' existe")
    session = Session()
    produto = session.query(Produto).filter(Produto.nome == produto_nome).first()
    
    
    if not produto:
        error_msg = "Produto não encontrado na base :/"
        logger.warning(f"Erro ao buscar o produto '{produto_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    
    try:
        produto.nome = form.nome
        produto.quantidade = form.quantidade
        produto.valor = form.valor
        session.commit()
        logger.debug(f"Produto '{produto_nome}' alterado")
        return apresenta_produto(produto), 200

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar a alteração :/"
        logger.warning(f"Erro ao salvar alteração, {error_msg}")
        return {"mesage": error_msg}, 400
    
#VENDAS
    
@app.post('/venda', tags=[venda_tag], 
          responses={"200": ListaVendasSchema, "400": ErrorSchema})
def set_venda(form: VendaSchema):
    " Insere uma venda onde uma venda pode ter varios produtos com o mesmo venda_id e cliente_id"
    session = Session()
    
    #Verifica a existencia do produto
    produto_id = form.produto_id
    logger.debug(f"Verificando se o produto #{produto_id} existe")
    produto = session.query(Produto).filter(Produto.id == produto_id).first()

    if not produto:
        error_msg = "Produto não encontrado na base :/"
        logger.warning(f"Erro ao buscar o produto '{produto_id}', {error_msg}")
        return {"mesage": error_msg}, 404
    
    if form.quantidade > produto.quantidade:
        error_msg = 'Produto insuficiente'
        return {'error': error_msg, 
                'Quantidade': f"Tem {produto.quantidade} produtos atualmente"}, 400
    
    produto.quantidade = produto.quantidade - form.quantidade
    
    #Verifica a existencia do cliente
    cliente_id = form.cliente_id
    logger.debug(f"Verificando se o cliente #{cliente_id} existe")
    cliente = session.query(Cliente).filter(Cliente.id == cliente_id).first()

    if not cliente:
        error_msg = "Cliente não encontrado na base :/"
        logger.warning(f"Erro ao buscar o cliente '{cliente_id}', {error_msg}")
        return {"mesage": error_msg}, 404
    
    venda = Venda(
        venda = form.venda_id,
        produto = form.produto_id,
        cliente = form.cliente_id,
        quantidade = form.quantidade,
        valor = produto.valor * float(form.quantidade))

    try:
        session.add(venda)
        session.commit()
        logger.debug(f"Adicionado venda de nome: '{venda.venda_id}'")
        return {"mesage": 'sucesso'}, 200

    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar venda '{venda.venda_id}', {error_msg}")
        return {"mesage": error_msg}, 400
    
@app.get('/venda/', tags=[venda_tag],
         responses={"200": VendaViewSchema, "404": ErrorSchema})
def get_venda(query: VendaBuscaSchema):
    "Realiza a busca de uma vendo podendo ser por data, cliente_id"
    logger.debug(f"Coletando vendas")
    session = Session()
    
    vendas = session.query(
        Venda.venda_id,
        Produto.nome,
        Venda.quantidade,
        Venda.valor,
        Venda.data_venda
    ).\
        join(Produto, Venda.produto_id == Produto.id).\
        join(Cliente, Venda.cliente_id == Cliente.id).\
        filter(Venda.cliente_id == query.cliente_id).all()
    print(vendas)
    if not vendas:
        error_msg = "Venda não encontrada na base :/"
        logger.warning(f"Erro ao buscar venda. {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Venda encontrada: ")
        return apresenta_vendas(vendas), 200
    
@app.get('/ultima-venda', tags=[venda_tag],
         responses={"200": VendaViewSchema, "404": ErrorSchema})
def get_vendas():
    """Faz a busca por todos as vendas cadastrados.
    """
    session = Session()
    vendas = session.query(Venda).order_by(Venda.venda_id.desc()).first()

    if not vendas:
        return {"vendas": 0}, 200
    else:
        print(vendas)
        return apresenta_ultima_venda(vendas), 200

