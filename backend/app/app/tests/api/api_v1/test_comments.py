# OpenPantheon: the pantheon for Education
# Copyright (C) 2021 CRI
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

def test_create_comment(client: TestClient, superuser_token_headers: dict, db: Session) -> None:
	data = {"author_id": "1", "personality_id": "1", "text": "This is a test comment", "fluff": "Here's a great link|http://google.fr~Here's another one|http://apple.com"}
	response = client.post(
		f"{settings.API_V1_STR}/comments/",
		headers=superuser_token_headers,
		json=data,
	)
	assert response.status_code == 200
	content = response.json()
	assert content["text"] == data["text"]
	assert content["fluff"] == data["fluff"]
	assert content["author_id"] == data["author_id"]
	assert content["personality_id"] == data["personality_id"]
