from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum

# Enums
class TipoTransacao(str, Enum):
    DEPOSITO = "deposito"
    SAQUE = "saque"

# Schemas de Usuário
class UsuarioCreate(BaseModel):
    username: str = Field(..., description="Nome de usuário único")
    password: str = Field(..., min_length=6, description="Senha com no mínimo 6 caracteres")

class Usuario(BaseModel):
    username: str

# Schemas de Autenticação
class Token(BaseModel):
    access_token: str
    token_type: str

# Schemas de Conta
class ContaCreate(BaseModel):
    titular: str = Field(..., description="Nome do titular da conta")
    
class Conta(BaseModel):
    id: int
    titular: str
    saldo: float
    data_criacao: datetime
    usuario: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "titular": "João Silva",
                "saldo": 1000.00,
                "data_criacao": "2025-11-12T10:00:00",
                "usuario": "joao"
            }
        }

# Schemas de Transação
class TransacaoCreate(BaseModel):
    conta_id: int = Field(..., description="ID da conta")
    tipo: TipoTransacao = Field(..., description="Tipo da transação: deposito ou saque")
    valor: float = Field(..., gt=0, description="Valor da transação (deve ser positivo)")
    
    class Config:
        json_schema_extra = {
            "example": {
                "conta_id": 1,
                "tipo": "deposito",
                "valor": 100.00
            }
        }

class Transacao(BaseModel):
    id: int
    conta_id: int
    tipo: TipoTransacao
    valor: float
    data: datetime
    saldo_apos_transacao: float
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "conta_id": 1,
                "tipo": "deposito",
                "valor": 100.00,
                "data": "2025-11-12T10:00:00",
                "saldo_apos_transacao": 1100.00
            }
        }

# Schema de Extrato
class Extrato(BaseModel):
    conta: Conta
    transacoes: list[Transacao]
    total_depositos: float
    total_saques: float