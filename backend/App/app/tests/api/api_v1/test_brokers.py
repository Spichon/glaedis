from fastapi.testclient import TestClient
from app.core.config import settings


def test_brokers_created(client: TestClient, user_token_headers: dict) -> None:
    available_brokers = []
    with open('app/db/ccxt_available_broker.txt') as f:
        available_brokers = f.read().splitlines()
    response = client.get(
        f"{settings.API_V1_STR}/brokers", headers=user_token_headers)
    assert response.status_code == 200
    content = response.json()
    created_broker = []
    for e in content:
        created_broker.append(e['name'].lower())
    for e in available_brokers:
        assert e in created_broker


