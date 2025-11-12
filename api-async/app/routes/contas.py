from fastapi import APIRouter, HTTPException, Depends, status
from datetime import datetime
from app.schemas import ContaCreate, Conta
from app.auth import get_current_user
from app.database import contas_db, proximo_id_conta

router = APIRouter()

@router.post("/", response_model=Conta, status_code=status.HTTP_201_CREATED)
async def criar_conta(conta: ContaCreate, current_user: str = Depends(get_current_user)):
    global proximo_id_conta
    
    from app import database
    
    nova_conta = {
        "id": database.proximo_id_conta,
        "titular": conta.titular,
        "saldo": 0.0,
        "data_criacao": datetime.now(),
        "usuario": current_user
    }
    
    contas_db[database.proximo_id_conta] = nova_conta
    database.proximo_id_conta += 1
    
    return nova_conta

@router.get("/", response_model=list[Conta])
async def listar_contas(current_user: str = Depends(get_current_user)):
    contas_usuario = [
        conta for conta in contas_db.values()
        if conta["usuario"] == current_user
    ]
    return contas_usuario

@router.get("/{conta_id}", response_model=Conta)
async def obter_conta(conta_id: int, current_user: str = Depends(get_current_user)):
    if conta_id not in contas_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conta não encontrada"
        )
    
    conta = contas_db[conta_id]
    
    # Verifica se a conta pertence ao usuário
    if conta["usuario"] != current_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Você não tem permissão para acessar esta conta"
        )
    
    return conta