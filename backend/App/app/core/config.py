from typing import Optional, Dict, Any, List, Union
import secrets
from pydantic import BaseSettings, PostgresDsn, validator, AnyHttpUrl
from starlette.datastructures import CommaSeparatedStrings
import os


class Settings(BaseSettings):
    ALLOWED_HOSTS = CommaSeparatedStrings(os.getenv("ALLOWED_HOSTS", ""))
    API_V1_STR = "/api/v1"
    PROJECT_NAME: str

    COGNITO_USER_POOL_ID: str
    COGNITO_USER_POOL_CLIENT_ID: str
    COGNITO_REGION: str

    DB_URL: str
    DB_URL_REPLICA: str
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("DB_USER"),
            password=values.get("DB_PASSWORD"),
            host=values.get("DB_URL"),
            path=f"/{values.get('DB_NAME') or ''}",
        )

    SECRET_KEY: str = secrets.token_urlsafe(32)

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost", "http://localhost:4200", "http://localhost:3000",
                                              "http://localhost:8080", "https://localhost", "https://localhost:4200",
                                              "https://localhost:3000", "https://localhost:8080",
                                              "http://localhost:5000",
                                              "http://www.dev.glaedis.com", "https://www.dev.glaedis.com",
                                              "https://www.glaedis.com", "http://local.dockertoolbox.glaedis.com",
                                              "http://localhost.glaedis.com"]

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)


settings = Settings()
