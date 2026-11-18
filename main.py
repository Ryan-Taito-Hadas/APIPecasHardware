from fastapi import FastAPI, HTTPException, Depends, status, Path
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Session

import models
from database import get_db
from security import criar_token, verificar_senha, get_current_user

app = FastAPI(
    title="API de Inventário de Hardware",
    description="API para gerenciar peças de hardware, com cadastro, consulta, atualização e exclusão.",
    version="1.0.0"
)
class PecaEntrada(BaseModel):
    nome: str
    categoria: str
    preco: float
    quantidade: int


class PecaResposta(PecaEntrada):
    id: int
    model_config = ConfigDict(from_attributes=True)


@app.get(
    "/",
    summary="Página inicial",
    description="Retorna uma mensagem de apresentação da API.",
    tags=["Geral"]
)
def inicio():
    """Exibe uma mensagem inicial da API."""
    return {"mensagem": "API de Inventario de Hardware"}

@app.post(
    "/login",
    summary="Realizar login",
    description="Autentica o usuário e retorna um token JWT para acessar as rotas protegidas.",
    tags=["Autenticação"],
    responses={
        401: {"description": "Email ou senha incorretos"}
    }
)

def login(dados: OAuth2PasswordRequestForm = Depends(),
          db: Session = Depends(get_db)):
    """Autentica o usuário e gera um token de acesso."""

    usuario = db.query(models.Usuario).filter(
        models.Usuario.email == dados.username
    ).first()

    if not usuario or not verificar_senha(
        dados.password, usuario.senha_hash
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos",
            headers={"WWW-Authenticate": "Bearer"}
        )

    token = criar_token(usuario.email)

    return {"access_token": token, "token_type": "bearer"}

@app.get(
    "/pecas",
    response_model=list[PecaResposta],
    summary="Listar peças",
    description="Retorna todas as peças cadastradas no inventário.",
    tags=["Peças"]
)

def listar_pecas(db: Session = Depends(get_db)):
    """Lista todas as peças cadastradas no inventário."""
    return db.query(models.Peca).all()


@app.get(
    "/pecas/{id}",
    response_model=PecaResposta,
    summary="Buscar peça por ID",
    description="Localiza uma peça específica pelo seu identificador.",
    tags=["Peças"],
    responses={
        404: {"description": "Peça não encontrada"}
    }
)

def buscar_peca(
    id: int = Path(..., description="Identificador da peça que será consultada"),
    db: Session = Depends(get_db)):
    """Busca uma peça específica pelo ID."""
    peca = db.query(models.Peca).filter(models.Peca.id == id).first()

    if not peca:
        raise HTTPException(status_code=404, detail="Peca nao encontrada")

    return peca


@app.post(
    "/pecas",
    response_model=PecaResposta,
    summary="Cadastrar peça",
    description="Cadastra uma nova peça no inventário. Requer autenticação.",
    tags=["Peças"],
    responses={
        401: {"description": "Token ausente ou inválido"}
    }
)

def criar_peca(peca: PecaEntrada,
               db: Session = Depends(get_db),
               usuario: models.Usuario = Depends(get_current_user)):
    """Cadastra uma nova peça no inventário."""
    nova_peca = models.Peca(**peca.model_dump())

    db.add(nova_peca)
    db.commit()
    db.refresh(nova_peca)

    return nova_peca


@app.put(
    "/pecas/{id}",
    response_model=PecaResposta,
    summary="Atualizar peça",
    description="Atualiza os dados de uma peça existente. Requer autenticação.",
    tags=["Peças"],
    responses={
        401: {"description": "Token ausente ou inválido"},
        404: {"description": "Peça não encontrada"}
    }
)

def atualizar_peca(id: int= Path(..., description="Identificador da peça que será atualizada"), 
                   dados: PecaEntrada = ...,
                   db: Session = Depends(get_db),
                   usuario: models.Usuario = Depends(get_current_user)):
    """Atualiza os dados de uma peça pelo ID."""
    peca = db.query(models.Peca).filter(models.Peca.id == id).first()

    if not peca:
        raise HTTPException(status_code=404, detail="Peca nao encontrada")

    for campo, valor in dados.model_dump().items():
        setattr(peca, campo, valor)

    db.commit()
    db.refresh(peca)

    return peca


@app.delete(
    "/pecas/{id}",
    summary="Excluir peça",
    description="Remove uma peça do inventário. Requer autenticação.",
    tags=["Peças"],
    responses={
        401: {"description": "Token ausente ou inválido"},
        404: {"description": "Peça não encontrada"}
    }
)

def excluir_peca(id: int = Path(..., description="Identificador da peça que será excluída"),
                 db: Session = Depends(get_db),
                 usuario: models.Usuario = Depends(get_current_user)):
    """Exclui uma peça do inventário pelo ID."""

    peca = db.query(models.Peca).filter(models.Peca.id == id).first()

    if not peca:
        raise HTTPException(status_code=404, detail="Peca nao encontrada")

    db.delete(peca)
    db.commit()

    return {"mensagem": "Peca excluida"}