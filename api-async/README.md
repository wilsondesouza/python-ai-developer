# 🏦 API Bancária Assíncrona

Uma API RESTful moderna desenvolvida com FastAPI para gerenciar operações bancárias como depósitos, saques e consulta de extratos. Este projeto implementa autenticação JWT e segue as melhores práticas de desenvolvimento de APIs.

## 📋 Funcionalidades

- ✅ **Autenticação JWT**: Sistema seguro de login e registro de usuários
- 💳 **Gestão de Contas**: Criação e consulta de contas correntes
- 💰 **Transações Bancárias**: Depósitos e saques com validações
- 📊 **Extrato Detalhado**: Visualização completa de todas as transações
- 🔒 **Segurança**: Proteção de rotas com tokens JWT
- 📝 **Documentação Automática**: Interface Swagger disponível

## 🚀 Tecnologias Utilizadas

- **FastAPI**: Framework web moderno e rápido
- **Pydantic**: Validação de dados
- **python-jose**: Implementação de JWT
- **passlib**: Criptografia de senhas
- **uvicorn**: Servidor ASGI

## 📁 Estrutura do Projeto

```
api-async/
├── app/
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py          # Rotas de autenticação
│   │   ├── contas.py        # Rotas de contas
│   │   └── transacoes.py    # Rotas de transações
│   ├── __init__.py
│   ├── auth.py              # Lógica de autenticação JWT
│   ├── config.py            # Configurações da aplicação
│   ├── database.py          # Banco de dados em memória
│   └── schemas.py           # Modelos Pydantic
├── main.py                  # Ponto de entrada da aplicação
├── requirements.txt         # Dependências do projeto
└── .gitignore
```

## ⚙️ Instalação e Configuração

### Dependências

```bash
fastapi
uvicorn
pydantic
python-jose[cryptography]
passlib[bcrypt].4
python-multipart
```

### Passo a Passo

1. **Clone o repositório**
```bash
git clone <url-do-repositorio>
cd api-async
```

2. **Crie e Ative um ambiente virtual**
```bash
python -m venv venv
venv\Scripts\activate
```

5. **Instale as dependências**
```bash
pip install -r requirements.txt
```

5. **Execute a aplicação**
```bash
uvicorn main:app --reload
```

A API estará disponível em: `http://localhost:8000`

## 📖 Documentação da API

Após iniciar o servidor, acesse:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🛡️ Validações Implementadas

- ✅ Senhas devem ter no mínimo 6 caracteres
- ✅ Valores de transações devem ser positivos
- ✅ Saques só são permitidos com saldo suficiente
- ✅ Usuários só podem acessar suas próprias contas
- ✅ Tokens JWT expiram em 30 minutos

## 🔒 Segurança

- Senhas são criptografadas usando bcrypt
- Autenticação via JWT (JSON Web Tokens)
- Rotas protegidas requerem token válido
- Validação de propriedade de contas

## 💡 Observações

- **Banco de Dados**: Esta versão utiliza armazenamento em memória. Os dados são perdidos quando o servidor é reiniciado.