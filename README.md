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
    
3. Crie e ative um ambiente virtual (opcional, mas recomendado):
    - **No Windows:**
        ```
        python -m venv nome_do_ambiente
        nome_do_ambiente\Scripts\activate
        ```
    - **No macOS e Linux:**
        ```
        python3 -m venv nome_do_ambiente
        source nome_do_ambiente/bin/activate
        ```

4. Instale as dependências:
    ```
    pip install -r requirements.txt
    ```

5. Execute as migrações do banco de dados:
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

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Contato

Para mais informações, entre em contato:

<a href="https://www.linkedin.com/in/arthur-ribeiro-peixoto-3b0096232/" target="_blank">![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)</a>
<a href="mailto:dev.arthur15@gmail.com">![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)</a>
<a href="https://www.instagram.com/arthurr2415" target="_blank">![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=Instagram&logoColor=white)</a>

