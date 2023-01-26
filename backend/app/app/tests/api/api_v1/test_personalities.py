# OpenPantheon: the pantheon for Education
# Copyright (C) 2022 Learning Planet Institute
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
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
