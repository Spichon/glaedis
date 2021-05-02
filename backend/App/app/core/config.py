from pydantic import BaseSettings
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


settings = Settings()
