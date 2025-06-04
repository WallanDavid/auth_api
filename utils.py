# utils.py

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

# Função para verificar o token JWT (exemplo)
def verify_token(token: str = Depends(OAuth2PasswordBearer)):
    try:
        # Implementar a verificação do JWT aqui
        pass
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")
