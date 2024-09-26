# Front-end IntelBiz

Sistema de ponto de venda desenvolvido para uma empresa ficticia chamada IntelBiz.

O sistema foi pensado e desenvolvido para ajudar a empresa a registrar suas vendas, estoque e também dar uma visão para o empreendedor de quem são os clientes que estão comprando os produtos.

---

## Como executar (Sem o docker)

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

## Como executar (Com o docker)

    1 - Certifique-se de ter o Docker instalado e em execução em sua máquina.

    2 - Depois de clonar o repositório do github, navegue até a pasta utilizando o CMD (Prompt de comando ou terminal da sua preferência) ou você pode abrir a pasta do projeto no `Visual Studio Code` e apertar `CTRL + Aspas`. Esse comando abrirá um console que já estará na pasta do projeto.

    3 - Execute o seguinte comando para construir a imagem Docker:
        docker build -t back-end-intelbiz .

    4 - Depois de criar a imagem, basta executar o container executando o comando a seguir:
        docker run -p 5000:5000 back-end-intelbiz


## Como abrir a documentação.

Abra o (http://localhost:5000/) ou (127.0.0.1:5000) no navegador para verificar o status da API em execução.
