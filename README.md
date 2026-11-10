Inventário de Hardware

API REST para gerenciar peças de computador, desenvolvida com Python e FastAPI.

Funcionalidades

Cadastrar peças

Listar todas as peças

Buscar peça por ID

Atualizar peças

Excluir peças

Tecnologias utilizadas

Python

FastAPI

Pydantic

SQLAlchemy

SQLite

Alembic

Como executar o projeto

Instale o Python.

Abra o terminal na pasta do projeto.

Crie o ambiente virtual:

python -m venv .venv

Ative o ambiente virtual no Windows:

.\.venv\Scripts\Activate.ps1

Instale as dependências:

python -m pip install -r requirements.txt

Execute as migrações do banco de dados:

alembic upgrade head

Inicie a API:

python -m uvicorn main:app --reload

Acesse a documentação pelo navegador:

http://127.0.0.1:8000/docs

Observação

Os dados são armazenados em um banco de dados SQLite e permanecem salvos mesmo após o servidor ser reiniciado.

## Observação

Os dados são armazenados em memória e são perdidos quando o servidor é reiniciado.
