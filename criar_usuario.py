from database import SessionLocal
from models import Usuario
from security import criar_hash

db = SessionLocal()

email = input("Digite o email: ")
senha = input("Digite a senha: ")

usuario = Usuario(
    email=email,
    senha_hash=criar_hash(senha)
)

db.add(usuario)
db.commit()

print("Usuario criado com sucesso!")

db.close()