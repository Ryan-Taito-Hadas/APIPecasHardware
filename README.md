# Inventário de Hardware

API REST para gerenciar peças de computador, desenvolvida com Python e FastAPI.

## Funcionalidades

- Cadastrar peças
- Listar todas as peças
- Buscar peça por ID
- Atualizar peças
- Excluir peças
- Autenticação utilizando OAuth2 e JWT
- Proteção das rotas de cadastro, atualização e exclusão

## Tecnologias utilizadas

- Python
- FastAPI
- Pydantic
- SQLAlchemy
- SQLite
- Alembic
- OAuth2
- JWT
- Argon2

## Como executar o projeto

1. Instale o Python.
2. Abra o terminal na pasta do projeto.
3. Crie o ambiente virtual:

   `python -m venv .venv`

4. Ative o ambiente virtual no Windows:

   `.\.venv\Scripts\Activate.ps1`

5. Instale as dependências:

   `python -m pip install -r requirements.txt`

6. Gere uma chave secreta:

   `python -c "import secrets; print(secrets.token_hex(32))"`

7. Crie um arquivo `.env` na pasta principal e adicione:

   `SECRET_KEY=sua_chave_gerada`

8. Execute as migrações do banco de dados:

   `alembic upgrade head`

9. Crie um usuário:

   `python criar_usuario.py`

10. Inicie a API:

   `python -m uvicorn main:app --reload`

11. Acesse a documentação pelo navegador:

   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Como testar a autenticação

1. Acesse `POST /login`.
2. Informe o e-mail no campo `username` e a senha.
3. Execute o login para receber o token JWT.
4. Clique em `Authorize` e informe suas credenciais.
5. Execute as rotas protegidas utilizando o token gerado.

## Observação

Os dados são armazenados em um banco de dados SQLite e permanecem salvos mesmo após o servidor ser reiniciado.

As rotas GET são públicas. As rotas POST, PUT e DELETE exigem autenticação.

O arquivo `.env`, que contém a chave secreta, não deve ser enviado ao GitHub.
