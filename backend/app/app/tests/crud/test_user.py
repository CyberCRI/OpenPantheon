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
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import crud
from app.core.security import verify_password
from app.schemas.user import UserCreate, UserUpdate
from app.tests.utils.utils import random_email, random_lower_string


def test_create_user(db: Session) -> None:
    first_name = random_lower_string()
    last_name = random_lower_string()
    email = random_email()
    password = random_lower_string()
    user_in = UserCreate(first_name=first_name, last_name=last_name, email=email, password=password)
    user = crud.user.create(db, obj_in=user_in)
    assert user.email == email
    assert hasattr(user, "hashed_password")


def test_authenticate_user(db: Session) -> None:
    first_name = random_lower_string()
    last_name = random_lower_string()
    email = random_email()
    password = random_lower_string()
    user_in = UserCreate(first_name=first_name, last_name=last_name, email=email, password=password)
    user = crud.user.create(db, obj_in=user_in)
    authenticated_user = crud.user.authenticate(db, email=email, password=password)
    assert authenticated_user
    assert user.email == authenticated_user.email


def test_not_authenticate_user(db: Session) -> None:
    email = random_email()
    password = random_lower_string()
    user = crud.user.authenticate(db, email=email, password=password)
    assert user is None


def test_check_if_user_is_active(db: Session) -> None:
    first_name = random_lower_string()
    last_name = random_lower_string()
    email = random_email()
    password = random_lower_string()
    user_in = UserCreate(first_name=first_name, last_name=last_name, email=email, password=password)
    user = crud.user.create(db, obj_in=user_in)
    is_active = crud.user.is_active(user)
    assert is_active is True


def test_check_if_user_is_active_inactive(db: Session) -> None:
    first_name = random_lower_string()
    last_name = random_lower_string()
    email = random_email()
    password = random_lower_string()
    user_in = UserCreate(first_name=first_name, last_name=last_name, email=email, password=password, disabled=True)
    user = crud.user.create(db, obj_in=user_in)
    is_active = crud.user.is_active(user)
    assert is_active


def test_check_if_user_is_superuser(db: Session) -> None:
    first_name = random_lower_string()
    last_name = random_lower_string()
    email = random_email()
    password = random_lower_string()
    user_in = UserCreate(first_name=first_name, last_name=last_name, email=email, password=password, is_superuser=True)
    user = crud.user.create(db, obj_in=user_in)
    is_superuser = crud.user.is_superuser(user)
    assert is_superuser is True


def test_check_if_user_is_superuser_normal_user(db: Session) -> None:
    first_name = random_lower_string()
    last_name = random_lower_string()
    username = random_email()
    password = random_lower_string()
    user_in = UserCreate(first_name=first_name, last_name=last_name, email=username, password=password)
    user = crud.user.create(db, obj_in=user_in)
    is_superuser = crud.user.is_superuser(user)
    assert is_superuser is False


def test_get_user(db: Session) -> None:
    first_name = random_lower_string()
    last_name = random_lower_string()
    password = random_lower_string()
    username = random_email()
    user_in = UserCreate(first_name=first_name,
                         last_name=last_name,
                         email=username,
                         password=password,
                         is_superuser=True)
    user = crud.user.create(db, obj_in=user_in)
    user_2 = crud.user.get(db, id=user.id)
    assert user_2
    assert user.email == user_2.email
    assert jsonable_encoder(user) == jsonable_encoder(user_2)


def test_update_user(db: Session) -> None:
    first_name = random_lower_string()
    last_name = random_lower_string()
    password = random_lower_string()
    email = random_email()
    user_in = UserCreate(first_name=first_name, last_name=last_name, email=email, password=password, is_superuser=True)
    user = crud.user.create(db, obj_in=user_in)
    new_password = random_lower_string()
    user_in_update = UserUpdate(password=new_password, is_superuser=True)
    crud.user.update(db, db_obj=user, obj_in=user_in_update)
    user_2 = crud.user.get(db, id=user.id)
    assert user_2
    assert user.email == user_2.email
    assert verify_password(new_password, user_2.hashed_password)
