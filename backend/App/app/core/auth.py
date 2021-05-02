import requests
from app.core.config import settings
from app.core.JWTBearer import JWKS, JWTBearer, JWTAuthorizationCredentials
jwks = JWKS.parse_obj(
    requests.get(
        f"https://cognito-idp.{settings.COGNITO_REGION}.amazonaws.com/"
        f"{settings.COGNITO_USER_POOL_ID}/.well-known/jwks.json"
    ).json()
)

auth = JWTBearer(jwks)

