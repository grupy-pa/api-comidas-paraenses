# Coding Dojo: API Rest com Python

## Objetivo

Este repositório tem como objetivo propor um desafio para dojos de python com Django

### O que será feito ?

ROUND 1: Preparação do projeto

No primeiro round será feita a preparação do projeto, os participantes terão que instalar o Django, iniciar um novo projeto e iniciar o servidor de testes a partir do manage.py

ROUND 2: Django Rest Framework

No segundo round os participantes terão que instalar o Django Rest Framework, configurar o DRF no projeto Django e testar sua configuração!

ROUND 3: Modelagem do banco de dados

No terceiro round os participantes irão modelar o banco de dados, criar o modelo ComidasParaenses, gerar as migrações e aplicar as migrações no banco.
Vamos utilizar o banco de dados SQLite3 e acessar o projeto https://inloop.github.io/sqlite-viewer/ para visualizar a estrutura do banco de dados.


ROUND 4: Criação das ViewSets e Serializers sem modelo

No quarto round os participantes terão que construir a primeira viewsets que deve ser construída sem modelo para que as urls da API possam ser configuradas e testadas via browser.

A URL deve ser algo do tipo: `GET /api/v1/receitas-paraenses/sobre` e deve retornar o status de HTTP 200 OK

ROUND 5: Criação das ViewSets e Serializers com modelo e testando o CRUD automático do DRF com o Thunder Client

Nesse round os participantes terão que construir o serializador de dados de modelos e também terão que codificar a ViewSets de modelo fornecendo ao DRF o poder de realizar o CRUD no banco de dados.
Também terão que utilizar a extensão do visual code Thunder Client para testar o CRUD na API

ROUND 6: TDD

Test Driven Developer: Desenvolvimento guiado por testes.
No sexto round os participantes terão que construir casos de testes que devem garantir que as urls funcionem e o output de dados esteja correto.

As chamadas para a url `GET /api/v1/receitas-paraenses/` devem retornar o código HTTP 200 OK

Testes de lista de comidas

Na rota `GET /api/v1/receitas-paraenses/` a api deve retornar uma lista contendo os objetos em um formato específico:

```json
[
  {
    "nome": "Tacacá",
    "descricao": "Tacacá é um prato típico da culinária amazônica, especialmente do estado do Pará, no Brasil. É conhecido por seu caldo quente feito com tucupi (um líquido amarelo extraído da mandioca brava), goma de tapioca, camarão seco e jambu, uma erva que causa uma sensação de dormência na boca.",
    "url_imagem": "https://"
  },
  {
    "nome": "Pato no tucupi",
    "descricao": "Pato no tucupi é um prato típico da culinária amazônica, originário do estado do Pará, no Brasil. É preparado com carne de pato cozida em um caldo amarelo chamado tucupi, que é extraído da mandioca brava, e enriquecido com jambu, uma erva típica da região que causa uma leve dormência na boca. ",
    "url_imagem": "https://"
  }
]
```

Teste pega comida

A rota `GET /api/v1/receitas-paraenses/<id-comida>` deve retornar um objeto JSON no formato específico:

```json
{
  "nome": "Tacacá",
  "descricao": "Tacacá é um prato típico da culinária amazônica, especialmente do estado do Pará, no Brasil. É conhecido por seu caldo quente feito com tucupi (um líquido amarelo extraído da mandioca brava), goma de tapioca, camarão seco e jambu, uma erva que causa uma sensação de dormência na boca.",
  "url_imagem": "https://"
}
```

ROUND 8: Django Admin

No último round os participantes terão que configurar a interface visual do Django Admin para gerenciar as receitas, permitando assim um operação de CRUD na interface visual do Django Admin.

Nos minutos finais da timebox será feita uma pequena retrospectiva do que foi desenvolvido e o que foi codificado será enviado para o repo do GruPy PA e ficará disponível para quem quiser e puder contribuir para melhorar!

Você pode utilizar este guia para estudar e praticar por conta própria :)