from fastapi import APIRouter, HTTPException, status
from app.schemas import UsuarioCreate, Token
from app.auth import hash_password, verify_password, create_access_token
from app.database import usuarios_db

router = APIRouter()

@router.post("/registro", response_model=dict, status_code=status.HTTP_201_CREATED)
async def registrar_usuario(usuario: UsuarioCreate):
    # Verifica se o usuário já existe
    if usuario.username in usuarios_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuário já existe"
        )
    
    # Cria o novo usuário
    usuarios_db[usuario.username] = {
        "username": usuario.username,
        "password": hash_password(usuario.password)
    }
    
    return {"mensagem": f"Usuário {usuario.username} registrado com sucesso!"}

@router.post("/login", response_model=Token)
async def login(usuario: UsuarioCreate):
    # Verifica se o usuário existe
    if usuario.username not in usuarios_db:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou senha incorretos"
        )
    
    # Verifica a senha
    user_data = usuarios_db[usuario.username]
    if not verify_password(usuario.password, user_data["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou senha incorretos"
        )
    
    # Cria o token
    access_token = create_access_token(data={"sub": usuario.username})
    
    return {"access_token": access_token, "token_type": "bearer"}