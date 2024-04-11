# Documentação de código

## Contextualizando o projeto:
  O projeto está estruturado em uma arquitetura N camadas com a
divisão entre camadas de Presentation (camada que é responsável
por receber todas as requisições do usuário), Business (camada esta
que terá toda nossa regra de negócio, verificando as entradas e se válidas
chamará o objeto respónsável para executar a transação de dados com o Banco de Dados),
 Model(responsável por executar as transações com o Banco de dados utilizando) 
e por fim Infra(que guarda objetos que tem como objetivo configurar nosso sistema)

## Técnologias utilizadas:
FastAPI, MySQL, Docker, ShellScript

## 1. Primeiros passos
### Linux:
 * Para o uso do programa em linux você necessita apenas digitar
 o seguinte comando:
`` pip install -r requirements.txt
``
* após isto há a necessidade de rodar o seguinte comando para iniciar o banco de dados
``docker-compose up -d
``, para uma maior praticidade fora gerado um script para inicialização do banco de dados, localizado em: *scripts/init_data_base.sh*

### Windows:
* Para usuários de Windows terá que usar o container da imagem do projeto na seguinte ordem:
  1. ``docker build -t projeto-vaga-backend ``
  2. ``docker run -p 8080:8080 projeto-vaga-backend ``
* E por fim rodar o seguinte comando para iniciar o banco de dados ``docker-compose up -d``

## 2. Rotas
### O projeto possui as seguintes rotas:

### Swagger
### /docs

### Department:
### /department/ [POST]
#### Salva um novo Departamento
### /department/ [LIST]
#### Lista todos os Departmento

### Employee:
### /employee/ [POST]
#### Salva um novo Empregados
### /employee/ [LIST]
#### Lista todos Empregados

