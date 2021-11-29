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
from typing import Any

from fastapi import APIRouter, Body, Depends
from pydantic.networks import EmailStr

from app import models, schemas
from app.api import deps
from app.core.config import settings
from app.send_email import send_contact_email, send_test_email

router = APIRouter()


@router.post("/test-email/", response_model=schemas.Msg, status_code=201)
async def test_email(
        email_to: EmailStr,
        current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Test emails.
    """
    await send_test_email(email_to=email_to)
    return {"msg": "Test email sent"}


@router.post("/contact/", response_model=schemas.Msg, status_code=201)
async def contact_email(
        email_to: EmailStr = settings.EMAILS_CONTACT_TO,
        email: EmailStr = Body(...),
        reason: str = Body(...),
        text: str = Body(...),
        name: str = Body(...),
) -> Any:
    """
    Sends email.
    """
    await send_contact_email(email_to=email_to, email=email, reason=reason, text=text, name=name)
    return {"msg": "Email sent"}
