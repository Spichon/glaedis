from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.utils import random_lower_string


def test_create_account(
        client: TestClient, user_token_headers: dict, db: Session
) -> None:
    data = {
        "name": "kraken",
        "broker_id": 1,
        "api_key": random_lower_string(32),
        "secret_key": random_lower_string(32)
    }
    response = client.post(
        f"{settings.API_V1_STR}/accounts/", headers=user_token_headers, json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == data["name"]
    assert content["broker"]["id"] == data["broker_id"]
    assert "id" in content
    assert "owner_id" in content
    assert "private_status" in content
    assert "public_status" in content

def test_read_account(
        client: TestClient, user_token_headers: dict, db: Session
) -> None:
    data = {
        "name": "kraken",
        "broker_id": 1,
        "api_key": random_lower_string(32),
        "secret_key": random_lower_string(32)
    }
    response = client.post(
        f"{settings.API_V1_STR}/accounts/", headers=user_token_headers, json=data,
    )
    assert response.status_code == 200
    content = response.json()
    response = client.get(
        f"{settings.API_V1_STR}/accounts/{content['id']}", headers=user_token_headers,
    )
    content = response.json()
    assert content["name"] == data["name"]
    assert content["broker"]["id"] == data["broker_id"]
    assert "id" in content
    assert "owner_id" in content
    assert "private_status" in content
    assert "public_status" in content
