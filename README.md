# Front-end IntelBiz

Sistema de ponto de venda desenvolvido para uma empresa ficticia chamada IntelBiz.

O sistema foi pensado e desenvolvido para ajudar a empresa a registrar suas vendas, estoque e também dar uma visão para o empreendedor de quem são os clientes que estão comprando os produtos.

---

## Como executar

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

Para executar a API  basta executar:

```
(env)$ python -m flask run --host 0.0.0.0 --port 5000 
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte.

```
(env)$ python -m flask run --host 0.0.0.0 --port 5000  --reload
```

Abra o (http://localhost:5000/) ou (127.0.0.1:5000) no navegador para verificar o status da API em execução.
