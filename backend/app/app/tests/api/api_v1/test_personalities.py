from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.personality import create_random_personality


def test_create_personality(client: TestClient, superuser_token_headers: dict, db: Session) -> None:
    data = {"field": "Foo", "gender": "Fighters"}
    response = client.post(
        f"{settings.API_V1_STR}/personalities/",
        headers=superuser_token_headers,
        json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["field"] == data["field"]
    assert content["gender"] == data["gender"]
    assert "id" in content


def test_read_personality(client: TestClient, superuser_token_headers: dict, db: Session) -> None:
    personality = create_random_personality(db)
    response = client.get(
        f"{settings.API_V1_STR}/personalities/{personality.id}",
        headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["field"] == personality.field
    assert content["gender"] == personality.gender
    assert content["id"] == personality.id
