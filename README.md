# Coding Dojo: API Rest com Python

## Objetivo

Este repositório tem como objetivo propor um desafio para dojos de python com Django

### O que será feito ?

- **round 1: preparação do ambiente e criação do projeto**
  - No primeiro round os participantes deverão criar o ambiente virtual ativá-lo e criar o projeto em Django.
- **round 2: Django Rest Framework**
  - No segundo round os participantes terão de instalar e configurar o DRF e validar a configuração.

- **round 3: Modelagem do banco de dados**
  - No terceiro round os participantes terão que modelar o banco de dados, gerar as migrações e aplicar as migrações no banco de dados.

- **round 4: Criação de uma ViewSets sem modelo e configuração das rotas da API**
  - No quarto round do dojo os participantes terão que construid uma ViewSets sem modelo e fazer a configuração das rotas com rest_framework.
- **round 5: ViewSets e Serializers com modelo e testes com Thunder Client**
  - No quarto round do dojo os participantes terão que construid uma ViewSets sem modelo e fazer a configuração das rotas com rest_framework.

##### ROUND 1: Preparação do ambiente e criação do projeto
No primeiro round os participantes terão que criar o ambiente virtual para o projeto e o ambiente criado deverá ser ativado.

Criação do ambiente virtual

```sh
python -m venv venv
```

Ativação do ambiente virtual

```sh
source venv/bin/activate
```

Após a criação e ativação do ambiente virtual os participantes terão que instalar o Django, iniciar um novo projeto e iniciar o servidor de testes a partir do manage.py

Instalação do Django

```sh
pip install django
```

Criação do projeto

```sh
django-admin startproject comidasparaenses .
```

O projeto deve ficar com a seguinte estrutura:

<center>

![Imagem do servidor local Django](images/estrutura_projeto.png)

</center>


Iniciando o projeto:

```sh
python manage.py runserver
```

Agora é só acessar a URL http://localhost:8000/

<center>

![Imagem do servidor local Django](images/manage_py_runserver.png)

</center>

##### ROUND 2: Django Rest Framework

No segundo round os participantes terão que instalar o Django Rest Framework, configurar o DRF no projeto Django e testar sua configuração!

instalação do DRF

```sh
pip install djangorestframework
```

Para "plugar" o DRF no Django, acesse o arquivo `settings.py` de configurações do projeto:


Adicione o DRF na lista de apps instaladas


<center>

![Imagem do servidor local Django](images/adiciona_rest_frameworks_apps.png)

</center>


Agora, atualize o banco de dados com o comando migrate

```sh
python manage.py migrate
```


<center>

![Imagem do servidor local Django](images/primeira_migracoes.png)

</center>


Agora vamos adicionar uma linha de código no arquivo `comidasparaenses/urls.py`

Adicione a linha a seguir logo abaixo da importação do path:

```py
from rest_framework import routers
```

O arquivo deve ficar assim:


<center>

![Imagem do servidor local Django](images/primeiras_linhas_rest_framework.png)

</center>


Agora é só executar o servidor de testes novamente!

```sh
python manage.py runserver
```

Acessando a URL  http://localhost:8000 novamente deve aparecer a tela do Django, indicando que Django está pronto para uso e o DRF foi plugado corretamente!


<center>

![Imagem do servidor local Django](images/manage_py_runserver.png)

</center>


##### ROUND 3: Modelagem do banco de dados

No terceiro round os participantes irão modelar o banco de dados, criar o modelo ComidasParaenses, gerar as migrações e aplicar as migrações no banco.
Vamos utilizar o banco de dados SQLite3 e acessar o projeto https://inloop.github.io/sqlite-viewer/ para visualizar a estrutura do banco de dados.


Criar a app de receitas

```sh
python manage.py startapp comidas
```

A estrutura da app deve ficar nesse formato:

<center>

![Imagem do servidor local Django](images/estrutura_app_comida.png)

</center>

No Django as apps são como se fossem módulos do projeto, assim como o DRF é um módulo para trabalhar com APIs RestFull de forma mais simplificada, a app `comidas` irá lidar com as comidas que iremos criar e disponibilizar via requisição HTTP.

Toda app no Django corresponde a uma tabela no banco de dados, mas não se preocupe, não será necessário escrever nenhuma linha de SQL para criar a tabela e configurar os campos! O motor de ORM (Object-relational Mapping - Mapeamento Objeto-relacional) irá cuidar de tudo isso.

E sempre que uma nova app for criada ela precisa ser plugada no Django, assim como foi feito com o rest_framework

<center>

![Imagem do servidor local Django](images/app_comidas_lista_de_apps.png)

</center>


Agora vamos codificar o banco de dados, acesse o arquivo `comidas/models.py`, você verá que na primeira linha importou os `models`, ou modelos.

Os modelos são a camada de definição de dados que representam a estrutura das tabelas do seu banco de dados, como tipos de campos e nomes de tabelas e etc...

Todo modelo em Django precisa ser uma classe filha da classe Model para que o Django entanda que aquela classe se trata de uma tabela no banco de dados.

Vamos codificar o modelo `Comida`, para isso adicione o código abaixo no arquivo `comidas/models.py`

```py

class Comida(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    foto_url = models.URLField(max_length=300, blank=True, null=True)

```

Nesse caso estamos criando a classe `Comida`, ou seja, uma tabela no banco de dados. Essa classe possuí três colunas:

Campo | Tipo | Descrição
------|------|-----------
nome | String, tamanho máximo 100 caracteres| Nome da comida
descricao| Texto livre | Descrição da comida
foto_url | URL com no máximo 300 caracteres, pode ser nulo e pode ser vazio | URL da comida

Após a codificação é necessário executar duas ações: gerar as migrações do banco de dados e aplicar as migrações no banco de dados.

Para gerar as migrações, execute

```bash
python manage.py makemigrations
```

A saída deve ser algo semelhante a, indicando que a ação a ser executada é a criação de um novo Model:

```sh
Migrations for 'comidas':
  comidas/migrations/0001_initial.py
    + Create model Comida
```

E para aplicar as migrações, execute

```bash
python manage.py migrate
```

A saída deve indicar que a migração foi aplicada no banco de dados

```sh
Running migrations:
  Applying comidas.0001_initial... OK
```

Ótimo! o banco de dados foi criado!

Podemos utilizar o aplicativo https://inloop.github.io/sqlite-viewer/ para visualizar a tabela.

##### ROUND 4: Criação de uma ViewSets sem modelo

No quarto round os participantes terão que construir a primeira viewsets que deve ser construída sem modelo para que as urls da API possam ser configuradas e testadas via browser.

Acesse arquivo `comidas/views.py`

Criação de uma ViewSets sem modelo

```py
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

class ViewSetSobre(ViewSet):

    def list(self, request):
        serializer = SobreSerializer()
        return Response({ "message": "API funcionando!" }, status=status.HTTP_200_OK)
```

Configurando a url da api

```py
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from comidas.views import ViewSetSobre

router = routers.DefaultRouter()

router.register(r'sobre', ViewSetSobre, basename='sobre')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/receitas-paraenses/', include(router.urls)),
]
```

A URL deve ser algo do tipo: `GET /api/v1/receitas-paraenses/sobre` e deve retornar o status de HTTP 200 OK

##### ROUND 5: Criação das ViewSets e Serializers com modelo e testando o CRUD automático do DRF com o Thunder Client

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