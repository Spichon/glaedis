from typing import Dict, Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.session import SessionLocal
from app.main import app
from app.tests.utils.user import user_authentication_headers
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string


@pytest.fixture(scope="session")
def db() -> Generator:
    global username
    global password
    username = random_lower_string() + "@antispam.com"
    password = random_lower_string()
    create_random_user(username=username, password=password)
    yield SessionLocal()


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
def user_token_headers(client: TestClient, db: Session) -> Dict[str, str]:
    return user_authentication_headers(email=username, password=password)
