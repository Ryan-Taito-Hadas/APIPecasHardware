from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_inicio():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "mensagem": "API de Inventario de Hardware"
    }

def test_listar_pecas():
    response = client.get("/pecas")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_buscar_peca_inexistente():
    response = client.get("/pecas/999999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Peca nao encontrada"

def test_cadastrar_peca_sem_token():
    dados = {
        "nome": "GTX 1650",
        "categoria": "Placa de video",
        "preco": 800.0,
        "quantidade": 2
    }

    response = client.post("/pecas", json=dados)

    assert response.status_code == 401


def test_excluir_peca_sem_token():
    response = client.delete("/pecas/1")

    assert response.status_code == 401