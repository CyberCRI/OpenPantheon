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
from typing import Any, List

import requests
from fastapi import APIRouter, Body, Depends, Header, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings
from app.send_email import send_new_account_email

router = APIRouter()


@router.get("/", response_model=List[schemas.User])
def read_users(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
        current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve users.
    """
    return crud.user.get_multi(db, skip=skip, limit=limit)


@router.post("/", response_model=schemas.User)
async def create_user(
        *,
        db: Session = Depends(deps.get_db),
        user_in: schemas.UserCreate,
        current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new user.
    """
    user = crud.user.get_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = crud.user.create(db, obj_in=user_in)
    if settings.EMAILS_ENABLED and user_in.email:
        await send_new_account_email(email_to=user_in.email, username=user_in.email, password=user_in.password)
    return user  # noqa: R504


@router.put("/me", response_model=schemas.User)
def update_user_me(
        *,
        db: Session = Depends(deps.get_db),
        password: str = Body(None),
        first_name: str = Body(None),
        last_name: str = Body(None),
        email: EmailStr = Body(None),
        current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update own user.
    """
    current_user_data = jsonable_encoder(current_user)
    user_in = schemas.UserUpdate(**current_user_data)
    if password is not None:
        user_in.password = password
    if first_name is not None:
        user_in.first_name = first_name
    if last_name is not None:
        user_in.last_name = last_name
    if email is not None:
        user_in.email = email
    return crud.user.update(db, db_obj=current_user, obj_in=user_in)


@router.post("/me/pantheon/{personality_id}", response_model=schemas.User)
def user_add_personality(
        *,
        db: Session = Depends(deps.get_db),
        personality_id: int,
        current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update a pantheon.
    """
    user = crud.user.get(db=db, id=current_user.id)
    if not user:
        raise HTTPException(status_code=404, detail="Current user not found")
    personality = crud.personality.get(db=db, id=personality_id)
    if not personality:
        raise HTTPException(status_code=404, detail="Personality not found")
    crud.user.add_personality(db=db, db_obj=user, personality_add=personality)
    return user


@router.get("/me", response_model=schemas.User)
def read_user_me(
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get current user.
    """
    return current_user


@router.post("/open", response_model=schemas.User)
def create_user_open(
    *,
    db: Session = Depends(deps.get_db),
    password: str = Body(...),
    email: EmailStr = Body(...),
    firstname: str = Body(...),
    lastname: str = Body(...),
    job: str = Body(default=None),
    captcha: str = Header(default=None),
    organization: str = Body(default=None)
) -> Any:
    """
    Create new user without the need to be logged in.
    """
    if (settings.RECAPTCHA_ENABLED):
        if (captcha is None or captcha == ''):
            raise HTTPException(
                status_code=403,
                detail="Missing captcha token",
            )
        answer = requests.post('https://www.google.com/recaptcha/api/siteverify', {
            'secret': settings.RECAPTCHA_SITE_SECRET,
            'response': captcha
        }).json()
        if not answer['success'] and answer['action'] != 'register' and answer['score'] < 0.5:
            raise HTTPException(
                status_code=403,
                detail="Captcha failed",
            )
    if not settings.USERS_OPEN_REGISTRATION:
        raise HTTPException(
            status_code=403,
            detail="Open user registration is forbidden on this server",
        )
    user = crud.user.get_by_email(db, email=email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system",
        )
    user_in = schemas.UserCreate(password=password,
                                 email=email,
                                 first_name=firstname,
                                 last_name=lastname,
                                 job=job,
                                 organization=organization)
    user = crud.user.create(db, obj_in=user_in)
    if settings.EMAILS_ENABLED and user_in.email:
        send_new_account_email(email_to=user_in.email, username=user_in.email, password=user_in.password)
    return user  # noqa: R504


@router.get("/{user_id}", response_model=schemas.User)
def read_user_by_id(
        user_id: int,
        db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific user by id.
    """
    return crud.user.get(db, id=user_id)


@router.put("/{user_id}", response_model=schemas.User)
def update_user(
        *,
        db: Session = Depends(deps.get_db),
        user_id: int,
        user_in: schemas.UserUpdate,
        current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update a user.
    """
    user = crud.user.get(db, id=user_id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="The user with this username does not exist in the system",
        )
    return crud.user.update(db, db_obj=user, obj_in=user_in)
