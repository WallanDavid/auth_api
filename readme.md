# 🔐 FastAPI Auth API

API de autenticação desenvolvida com **FastAPI**, **JWT**, **Refresh Token** e banco **SQLite** via **SQLAlchemy**.

Ideal para projetos que precisam de:
- Login seguro com token
- Proteção de rotas
- Cadastro de usuários
- Refresh automático de sessão

## 🚀 Features

- [x] Login com JWT (`access_token` + `refresh_token`)
- [x] Cadastro de usuários (`/signup`)
- [x] Proteção de rotas com token (`/users/me`)
- [x] Banco real com SQLite (pronto pra PostgreSQL)
- [x] Documentação Swagger UI pronta para testes

## 📦 Tecnologias

- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite
- JWT (pyjwt)
- Passlib
- Pydantic
- Dotenv

## ▶️ Como rodar localmente

```bash
# 1. Clone o projeto
git clone https://github.com/WallanDavid/auth_api.git
cd auth_api

# 2. Crie ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Instale dependências
pip install -r requirements.txt

# 4. Crie o arquivo .env
```

### `.env` de exemplo:
```env
SECRET_KEY=sua_chave_super_secreta_aqui
DATABASE_URL=sqlite:///./app.db
```

```bash
# 5. Rode a API
uvicorn main:app --reload
```

Acesse: [http://localhost:8000/docs](http://localhost:8000/docs)

## 🔐 Endpoints principais

- `POST /signup` → cria novo usuário
- `POST /token` → login com username/senha
- `POST /refresh` → gera novo access token
- `GET /users/me` → retorna usuário autenticado

## ☁️ Deploy no Railway

1. Suba este projeto no GitHub
2. Acesse [railway.app](https://railway.app)
3. Crie um novo projeto e conecte o repositório
4. Adicione as variáveis de ambiente:
   - `SECRET_KEY`
   - `DATABASE_URL=sqlite:///./app.db`
5. Comando de start:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port $PORT
   ```
6. Acesse o link gerado: `https://seu-app.up.railway.app/docs`

## 👨‍💻 Autor

**Wallan David** – [@WallanDavid](https://github.com/WallanDavid)  
Back-end | Cloud | Infraestrutura | Desenvolvimento

## 📄 Licença

MIT — pode usar, adaptar e compartilhar com os créditos 😎
