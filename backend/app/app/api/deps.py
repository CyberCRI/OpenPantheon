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
from typing import Any, Generator

import requests
from fastapi import Depends, Header, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.core import security
from app.core.config import settings
from app.db.session import SessionLocal

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/login/access-token")


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_current_user(db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)) -> models.User:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[security.ALGORITHM])
        token_data = schemas.TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = crud.user.get(db, id=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_current_active_user(current_user: models.User = Depends(get_current_user), ) -> models.User:
    if not crud.user.is_active(current_user):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def get_current_active_superuser(current_user: models.User = Depends(get_current_user), ) -> models.User:
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="The user doesn't have enough privileges")
    return current_user


class CaptchaValidator:
    def __init__(self, action: str) -> None:
        self.action = action

    def _is_score_valid(self, response_body: Any) -> bool:
        return response_body['success'] and response_body[
            'action'] == self.action and response_body['score'] >= settings.RECAPTCHA_SCORE_THRESHOLD

    def __call__(self, captcha: str = Header(None)) -> None:
        if settings.RECAPTCHA_ENABLED:
            if captcha is None or captcha == '':
                raise HTTPException(
                    status_code=403,
                    detail="Missing captcha token",
                )
            response = requests.post('https://www.googlrequests.Responsee.com/recaptcha/api/siteverify', {
                'secret': settings.RECAPTCHA_SITE_SECRET,
                'response': captcha
            })
            if response.status_code >= 400 or not self._is_score_valid(response.json()):
                raise HTTPException(
                    status_code=403,
                    detail=f"Captcha failed for {self.action}",
                )
