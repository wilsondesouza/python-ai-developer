from fastapi import APIRouter, HTTPException, Depends, status
from datetime import datetime
from app.schemas import TransacaoCreate, Transacao, Extrato, TipoTransacao
from app.auth import get_current_user
from app.database import contas_db, transacoes_db

router = APIRouter()

@router.post("/", response_model=Transacao, status_code=status.HTTP_201_CREATED)
async def criar_transacao(transacao: TransacaoCreate, current_user: str = Depends(get_current_user)):
    # Verifica se a conta existe
    if transacao.conta_id not in contas_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Conta não encontrada"
        )
    
    conta = contas_db[transacao.conta_id]
    
    # Verifica se a conta pertence ao usuário
    if conta["usuario"] != current_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Você não tem permissão para acessar esta conta"
        )
    
    # Validação: valor positivo (já feito pelo Pydantic com gt=0)
    # Validação adicional para saques
    if transacao.tipo == TipoTransacao.SAQUE:
        if conta["saldo"] < transacao.valor:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Saldo insuficiente. Saldo atual: R$ {conta['saldo']:.2f}"
            )
        conta["saldo"] -= transacao.valor
    else:  # DEPOSITO
        conta["saldo"] += transacao.valor
    
    from app import database
    
    # Cria a transação
    nova_transacao = {
        "id": database.proximo_id_transacao,
        "conta_id": transacao.conta_id,
        "tipo": transacao.tipo,
        "valor": transacao.valor,
        "data": datetime.now(),
        "saldo_apos_transacao": conta["saldo"]
    }
    
    transacoes_db.append(nova_transacao)
    database.proximo_id_transacao += 1
    
    return nova_transacao

@router.get("/extrato/{conta_id}", response_model=Extrato)
async def obter_extrato(conta_id: int, current_user: str = Depends(get_current_user)):
    # Verifica se a conta existe
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
    
    # Filtra transações da conta
    transacoes_conta = [t for t in transacoes_db if t["conta_id"] == conta_id]
    
    # Calcula totais
    total_depositos = sum(t["valor"] for t in transacoes_conta if t["tipo"] == TipoTransacao.DEPOSITO)
    total_saques = sum(t["valor"] for t in transacoes_conta if t["tipo"] == TipoTransacao.SAQUE)
    
    return {
        "conta": conta,
        "transacoes": transacoes_conta,
        "total_depositos": total_depositos,
        "total_saques": total_saques
    }