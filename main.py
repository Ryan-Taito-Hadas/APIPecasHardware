
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class PecaEntrada(BaseModel):
    nome: str
    categoria: str
    preco: float
    quantidade: int

class Peca(PecaEntrada):
    id: int

pecas = []

@app.get("/")
def inicio():
    return {"mensagem": "API de Inventario de Hardware"}

@app.get("/pecas", response_model=list[Peca])
def listar_pecas():
    return pecas

@app.get("/pecas/{id}", response_model=Peca)
def buscar_peca(id: int):
    for peca in pecas:
        if peca["id"] == id:
            return peca
    raise HTTPException(status_code=404, detail="Peca nao encontrada")

@app.post("/pecas", response_model=Peca)
def criar_peca(peca: PecaEntrada):
    nova_peca = peca.model_dump()
    nova_peca["id"] = max([p["id"] for p in pecas], default=0) + 1
    pecas.append(nova_peca)
    return nova_peca

@app.put("/pecas/{id}", response_model=Peca)
def atualizar_peca(id: int, dados: PecaEntrada):
    for peca in pecas:
        if peca["id"] == id:
            peca.update(dados.model_dump())
            return peca
    raise HTTPException(status_code=404, detail="Peca nao encontrada")

@app.delete("/pecas/{id}")
def excluir_peca(id: int):
    for peca in pecas:
        if peca["id"] == id:
            pecas.remove(peca)
            return {"mensagem": "Peca excluida"}
    raise HTTPException(status_code=404, detail="Peca nao encontrada")

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class PecaEntrada(BaseModel):
    nome: str
    categoria: str
    preco: float
    quantidade: int

class Peca(PecaEntrada):
    id: int

pecas = []

@app.get("/")
def inicio():
    return {"mensagem": "API de Inventario de Hardware"}

@app.get("/pecas", response_model=list[Peca])
def listar_pecas():
    return pecas

@app.get("/pecas/{id}", response_model=Peca)
def buscar_peca(id: int):
    for peca in pecas:
        if peca["id"] == id:
            return peca
    raise HTTPException(status_code=404, detail="Peca nao encontrada")

@app.post("/pecas", response_model=Peca)
def criar_peca(peca: PecaEntrada):
    nova_peca = peca.model_dump()
    nova_peca["id"] = max([p["id"] for p in pecas], default=0) + 1
    pecas.append(nova_peca)
    return nova_peca

@app.put("/pecas/{id}", response_model=Peca)
def atualizar_peca(id: int, dados: PecaEntrada):
    for peca in pecas:
        if peca["id"] == id:
            peca.update(dados.model_dump())
            return peca
    raise HTTPException(status_code=404, detail="Peca nao encontrada")

@app.delete("/pecas/{id}")
def excluir_peca(id: int):
    for peca in pecas:
        if peca["id"] == id:
            pecas.remove(peca)
            return {"mensagem": "Peca excluida"}
    raise HTTPException(status_code=404, detail="Peca nao encontrada")
