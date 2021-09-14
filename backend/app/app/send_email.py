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
from pathlib import Path
from typing import Any, Dict

from fastapi_mail import ConnectionConfig, FastMail, MessageSchema
from pydantic import EmailStr

from app.core.config import settings

configuration = ConnectionConfig(MAIL_USERNAME=settings.SMTP_USER,
                                 MAIL_PASSWORD=settings.SMTP_PASSWORD,
                                 MAIL_FROM=settings.EMAILS_FROM_EMAIL,
                                 MAIL_FROM_NAME=settings.EMAILS_FROM_NAME,
                                 MAIL_PORT=settings.SMTP_PORT,
                                 MAIL_SERVER=settings.SMTP_HOST,
                                 MAIL_TLS=False,
                                 MAIL_SSL=settings.SMTP_TLS,
                                 VALIDATE_CERTS=True,
                                 USE_CREDENTIALS=True,
                                 TEMPLATE_FOLDER=Path(__file__).parent / "email-templates/build",
                                 SUPPRESS_SEND=not settings.EMAILS_ENABLED)


async def send_email(
    email_to: EmailStr,
    subject: str,
    template_name: str,
    template_body: Dict[str, Any],
) -> None:
    message = MessageSchema(subject=subject, recipients=[email_to], template_body=template_body)
    fastmail = FastMail(configuration)
    await fastmail.send_message(message, template_name=template_name)


async def send_test_email(email_to: EmailStr) -> None:
    project_name = settings.PROJECT_NAME
    subject = f"{project_name} - Test email"
    await send_email(
        email_to=email_to,
        subject=subject,
        template_name="test_email.html",
        template_body={
            "project_name": project_name,
            "email": email_to
        },
    )


async def send_reset_password_email(email_to: EmailStr, email: str, token: str) -> None:
    project_name = settings.PROJECT_NAME
    subject = f"{project_name} - Password recovery for user {email}"
    link = f"{settings.SERVER_HOST}/reset-password?token={token}"
    await send_email(
        email_to=email_to,
        subject=subject,
        template_name="reset_password.html",
        template_body={
            "project_name": project_name,
            "username": email,
            "email": email_to,
            "valid_hours": settings.EMAIL_RESET_TOKEN_EXPIRE_HOURS,
            "link": link,
        },
    )


async def send_new_account_email(email_to: EmailStr, username: str, password: str) -> None:
    project_name = settings.PROJECT_NAME
    subject = f"{project_name} - New account for user {username}"
    link = settings.SERVER_HOST
    await send_email(
        email_to=email_to,
        subject=subject,
        template_name="new_account.html",
        template_body={
            "project_name": settings.PROJECT_NAME,
            "username": username,
            "password": password,
            "email": email_to,
            "link": link,
        },
    )
