# API de Gerenciamento de Produtos

Este projeto é uma API RESTful desenvolvida em Django e Django REST Framework para gerenciar produtos. A API permite o cadastro, atualização, visualização e exclusão de produtos.

## Tecnologias Utilizadas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

## Funcionalidades

- Cadastro de produtos com nome, descrição, preço e quantidade em estoque.
- Atualização de produtos existentes.
- Visualização de produtos por ID.
- Listagem de todos os produtos cadastrados.
- Exclusão de produtos.

## Configuração do Ambiente

### Pré-requisitos

- Python 3.x
- pip
- Git

### Instalação

1. Clone o repositório:
    ```
    git clone https://github.com/ArthurRibeir0/Crud_Products.git
    ```

2. Navegue até o diretório do projeto:
    ```
    cd Crud_Products
    ```

3. Instale as dependências:
    ```
    pip install -r requirements.txt
    ```

4. Execute as migrações do banco de dados:
    ```
    python manage.py migrate
    ```

## Uso da API

### Endpoints

- **POST /api/products**: Cadastrar um novo produto.
- **PUT /api/products/{id}**: Atualizar um produto existente.
- **GET /api/products/{id}**: Visualizar detalhes de um produto por ID.
- **GET /api/products**: Listar todos os produtos cadastrados.
- **DELETE /api/products/{id}**: Excluir um produto por ID.

### Exemplos de Payload

#### Cadastrar Produto

```json
{
    "name": "Produto Teste",
    "description": "Descrição do Produto",
    "price": 100.00,
    "stock": 10
}
```

#### Atualizar Produto

```json
{
    "name": "Produto Teste Atualizado",
    "description": "Nova Descrição",
    "price": 150.00,
    "stock": 15
}
```

### Respostas

- **200 OK**: Sucesso na operação.
- **201 Created**: Produto cadastrado com sucesso.
- **400 Bad Request**: Erro de validação nos dados enviados.
- **404 Not Found**: Produto não encontrado.
- **500 Internal Server Error**: Erro interno do servidor.
