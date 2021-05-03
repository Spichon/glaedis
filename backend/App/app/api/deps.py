from fastapi import Depends, HTTPException
from starlette.status import HTTP_403_FORBIDDEN
from typing import Generator
from app.core.JWTBearer import JWTAuthorizationCredentials
from app.core.auth import auth
from app.schemas import User
from app.db.session import SessionLocal


async def get_current_user(
        credentials: JWTAuthorizationCredentials = Depends(auth)
) -> User:
    try:
        return {"username": credentials.claims["username"]}
    except KeyError:
        HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Username missing")


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
