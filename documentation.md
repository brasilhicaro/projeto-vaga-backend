# Documentação de código

## Contextualizando o projeto:
  O projeto está estruturado em uma arquitetura N camadas com a
divisão entre camadas de Presentation (camada que é responsável
por receber todas as requisições do usuário), Business (camada esta
que terá toda nossa regra de negócio, verificando as entradas e se válidas
chamará o objeto responsável para executar a transação de dados com o Banco de Dados),
 Model (responsável por executar as transações com o Banco de dados utilizando) 
e por fim Infra (que guarda objetos que têm como objetivo configurar nosso sistema).

## Tecnologias utilizadas:
#### FastAPI: O uso do FastAPI dá-se por sua praticidade e a implementação nativa de um Swagger.
#### PostgreSQL: O SGBD mais utilizado (portanto há mais conteúdo) e provém uma segurança e velocidade que é algo que almejo sempre que penso em algum Banco de dados.
#### Docker: O uso do Docker foi utilizado para garantir que independente do SO, a API sempre irá rodar o mesmo serviço sem riscos de conflito entre versões de ferramentas.
#### ShellScript: Para a execução da API diretamente pela inicialização do Docker-Compose.

## 1. Primeiros passos
### Configuração e Inicialização:
 * Para utilizar o programa será necessário ter na máquina o [Docker](https://www.docker.com/), todo o processo de configuração do Docker poderá ser encontrado no site oficial.
  * Com o Docker instalado e configurado, execute o seguinte comando: ``docker-compose up -d``.

## 2. Rotas
### O projeto possui as seguintes rotas:
#### Para mais detalhes de cada rota, é necessário acessar o Swagger utilizando /docs.
* Rotas POST: /department/ e /employee/
* Rotas LIST: /department/ e /employee/