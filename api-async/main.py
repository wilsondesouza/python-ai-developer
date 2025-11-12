from fastapi import FastAPI
from app.routes import auth, contas, transacoes

app = FastAPI(
    title="API Bancária Assíncrona",
    description="API para gerenciar operações bancárias de depósitos e saques",
    version="1.0.0"
)

# Incluindo as rotas
app.include_router(auth.router, prefix="/api/auth", tags=["Autenticação"])
app.include_router(contas.router, prefix="/api/contas", tags=["Contas"])
app.include_router(transacoes.router, prefix="/api/transacoes", tags=["Transações"])

@app.get("/")
async def root():
    return {
        "mensagem": "Bem-vindo à API Bancária!",
        "documentacao": "/docs"
    }
