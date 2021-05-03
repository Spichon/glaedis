from typing import Optional, Dict, Any

from pydantic import BaseSettings, PostgresDsn, validator
from starlette.datastructures import CommaSeparatedStrings
import os


class Settings(BaseSettings):
    ALLOWED_HOSTS = CommaSeparatedStrings(os.getenv("ALLOWED_HOSTS", ""))
    API_V1_STR = "/api/v1"
    PROJECT_NAME: str

    COGNITO_USER_POOL_ID: str
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


settings = Settings()
