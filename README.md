# Inventário de Hardware

API REST para gerenciar peças de computador, desenvolvida com Python e FastAPI.

## Funcionalidades

- Cadastrar peças
- Listar todas as peças
- Buscar peça por ID
- Atualizar peças
- Excluir peças

## Tecnologias utilizadas

- Python
- FastAPI
- Pydantic

## Como executar o projeto

1. Instale o Python.
2. Abra o terminal na pasta do projeto.
3. Crie o ambiente virtual:

   `python -m venv .venv`

4. Ative o ambiente virtual no Windows:

   `.\.venv\Scripts\Activate.ps1`

5. Instale as dependências:

   `python -m pip install -r requirements.txt`

6. Inicie a API:

   `python -m uvicorn main:app --reload`

7. Acesse a documentação pelo navegador:

   http://127.0.0.1:8000/docs

## Observação

Os dados são armazenados em memória e são perdidos quando o servidor é reiniciado.
