from fastapi.testclient import TestClient
from app.core.config import settings


def test_users_me(client: TestClient, user_token_headers: dict) -> None:
    response = client.get(
        f"{settings.API_V1_STR}/users/me", headers=user_token_headers)
    assert response.status_code == 200
