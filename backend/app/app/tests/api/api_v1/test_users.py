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
from typing import Dict

from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app import crud
from app.core.config import settings
from app.schemas.user import UserCreate
from app.tests.utils.utils import random_email, random_lower_string


def test_get_users_superuser_me(client: TestClient, superuser_token_headers: Dict[str, str]) -> None:
    r = client.get(f"{settings.API_V1_STR}/users/me", headers=superuser_token_headers)
    current_user = r.json()
    assert current_user
    assert current_user["is_active"] is True
    assert current_user["is_superuser"]
    assert current_user["email"] == settings.FIRST_SUPERUSER


def test_get_users_normal_user_me(client: TestClient, normal_user_token_headers: Dict[str, str]) -> None:
    r = client.get(f"{settings.API_V1_STR}/users/me", headers=normal_user_token_headers)
    current_user = r.json()
    assert current_user
    assert current_user["is_active"] is True
    assert current_user["is_superuser"] is False
    assert current_user["email"] == settings.EMAIL_TEST_USER


def test_create_user_new_email(client: TestClient, superuser_token_headers: dict, db: Session) -> None:
    first_name = random_lower_string()
    last_name = random_lower_string()
    username = random_email()
    password = random_lower_string()
    data = {"email": username, "password": password, "first_name": first_name, "last_name": last_name}
    r = client.post(
        f"{settings.API_V1_STR}/users/",
        headers=superuser_token_headers,
        json=data,
    )
    assert 200 <= r.status_code < 300
    created_user = r.json()
    user = crud.user.get_by_email(db, email=username)
    assert user
    assert user.email == created_user["email"]


def test_get_existing_user(client: TestClient, superuser_token_headers: dict, db: Session) -> None:
    first_name = random_lower_string()
    last_name = random_lower_string()
    username = random_email()
    password = random_lower_string()
    user_in = UserCreate(first_name=first_name, last_name=last_name, email=username, password=password)
    user = crud.user.create(db, obj_in=user_in)
    user_id = user.id
    r = client.get(
        f"{settings.API_V1_STR}/users/{user_id}",
        headers=superuser_token_headers,
    )
    assert 200 <= r.status_code < 300
    api_user = r.json()
    existing_user = crud.user.get_by_email(db, email=username)
    assert existing_user
    assert existing_user.email == api_user["email"]


def test_create_user_existing_username(client: TestClient, superuser_token_headers: dict, db: Session) -> None:
    first_name = random_lower_string()
    last_name = random_lower_string()
    username = random_email()
    password = random_lower_string()
    user_in = UserCreate(first_name=first_name, last_name=last_name, email=username, password=password)
    crud.user.create(db, obj_in=user_in)
    data = {
        "first_name": random_lower_string(),
        "last_name": random_lower_string(),
        "email": username,
        "password": password
    }
    r = client.post(
        f"{settings.API_V1_STR}/users/",
        headers=superuser_token_headers,
        json=data,
    )
    created_user = r.json()
    assert r.status_code == 400
    assert "_id" not in created_user


def test_create_user_by_normal_user(client: TestClient, normal_user_token_headers: Dict[str, str]) -> None:
    first_name = random_lower_string()
    last_name = random_lower_string()
    username = random_email()
    password = random_lower_string()
    data = {"email": username, "password": password, "first_name": first_name, "last_name": last_name}
    r = client.post(
        f"{settings.API_V1_STR}/users/",
        headers=normal_user_token_headers,
        json=data,
    )
    assert r.status_code == 400


def test_retrieve_users(client: TestClient, superuser_token_headers: dict, db: Session) -> None:
    first_name = random_lower_string()
    last_name = random_lower_string()
    username = random_email()
    password = random_lower_string()
    user_in = UserCreate(first_name=first_name, last_name=last_name, email=username, password=password)
    crud.user.create(db, obj_in=user_in)

    first_name2 = random_lower_string()
    last_name2 = random_lower_string()
    username2 = random_email()
    password2 = random_lower_string()
    user_in2 = UserCreate(first_name=first_name2, last_name=last_name2, email=username2, password=password2)
    crud.user.create(db, obj_in=user_in2)

    r = client.get(f"{settings.API_V1_STR}/users/", headers=superuser_token_headers)
    all_users = r.json()

    assert len(all_users) > 1
    for personality in all_users:
        assert "email" in personality
