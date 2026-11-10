from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Session
import models
from database import engine, get_db

app = FastAPI()

class PecaEntrada(BaseModel):
    nome: str
    categoria: str
    preco: float
    quantidade: int

class PecaResposta(PecaEntrada):
    id: int
    model_config = ConfigDict(from_attributes=True)

@app.get("/")
def inicio():
    return {"mensagem": "API de Inventario de Hardware"}

@app.get("/pecas", response_model=list[PecaResposta])
def listar_pecas(db: Session = Depends(get_db)):
    return db.query(models.Peca).all()

@app.get("/pecas/{id}", response_model=PecaResposta)
def buscar_peca(id: int, db: Session = Depends(get_db)):
    peca = db.query(models.Peca).filter(models.Peca.id == id).first()

    if not peca:
        raise HTTPException(status_code=404, detail="Peca nao encontrada")

    return peca

@app.post("/pecas", response_model=PecaResposta)
def criar_peca(peca: PecaEntrada, db: Session = Depends(get_db)):
    nova_peca = models.Peca(**peca.model_dump())

    db.add(nova_peca)
    db.commit()
    db.refresh(nova_peca)

    return nova_peca

@app.put("/pecas/{id}", response_model=PecaResposta)
def atualizar_peca(id: int, dados: PecaEntrada, db: Session = Depends(get_db)):
    peca = db.query(models.Peca).filter(models.Peca.id == id).first()

    if not peca:
        raise HTTPException(status_code=404, detail="Peca nao encontrada")

    for campo, valor in dados.model_dump().items():
        setattr(peca, campo, valor)

    db.commit()
    db.refresh(peca)

    return peca

@app.delete("/pecas/{id}")
def excluir_peca(id: int, db: Session = Depends(get_db)):
    peca = db.query(models.Peca).filter(models.Peca.id == id).first()

    if not peca:
        raise HTTPException(status_code=404, detail="Peca nao encontrada")

    db.delete(peca)
    db.commit()

    return {"mensagem": "Peca excluida"}