from fastapi import Depends, HTTPException
from starlette.status import HTTP_403_FORBIDDEN
from app.core.JWTBearer import JWTAuthorizationCredentials
from app.core.auth import auth
from app.schemas import User


async def get_current_user(
        credentials: JWTAuthorizationCredentials = Depends(auth)
) -> User:
    try:
        return {"username": credentials.claims["username"]}
    except KeyError:
        HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Username missing")
