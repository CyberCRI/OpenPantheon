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
from typing import Any, Dict, List, Optional, cast

from fastapi import APIRouter, Depends, HTTPException
from pydantic import EmailStr
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings
from app.models.comment import Comment
from app.send_email import send_comment_approved_email

router = APIRouter()


@router.post("/", response_model=schemas.Comment)
def create_comment(
        *,
        db: Session = Depends(deps.get_db),
        input: Optional[List[Dict]] = None,
        current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new comment.
    """
    comment_in = input[0]  # type: ignore
    del input[0]  # type: ignore
    fluff = input
    tab = []
    for i in range(len(fluff)):  # type: ignore
        tab.append(fluff[i]['name'] + '|' + fluff[i]['link'])  # type: ignore
    comment_in['fluff'] = '~'.join(tab)
    return crud.comment.create_new_comment(db=db, obj_in=comment_in)  # type: ignore


@router.get("/unapproved")
def get_unapprouved_comments(
        *,
        db: Session = Depends(deps.get_db),
        current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Get unapprouved comments
    """
    # The condition Comment.is_validated is False doesn't work
    return db.query(Comment).filter(Comment.is_validated == False).all()  # noqa: E712


@router.patch("/approve/{id}", response_model=schemas.Comment)
async def approve_comment(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Approve a Comment.
    """
    comment = crud.comment.get(db=db, id=id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    db_current_user = crud.user.get(db=db, id=comment.author_id)
    if db_current_user is None:
        raise HTTPException(status_code=400, detail="User not found")
    comment = crud.comment.approve(db=db, comment=comment)
    await send_comment_approved_email(
        email_to=cast(EmailStr, db_current_user.email),
        email=settings.EMAILS_CONTACT_TO,
        comment=comment.text if comment.text is not None else '',
        personality_id=comment.personality_id if comment.personality_id is not None else 0,
    )
    return comment


@router.delete("/{id}", response_model=schemas.Comment)
def delete_comment(
        *,
        db: Session = Depends(deps.get_db),
        id: int,
        current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete a Comment.
    """
    comment = crud.comment.get(db=db, id=id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    if current_user.id != comment.author_id and not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    crud.user.remove_personality(
        db=db,
        db_obj=crud.user.get(db=db, id=comment.author_id),  # type: ignore
        id_personality=comment.personality_id)  # type: ignore
    if len(crud.personality.get(db=db, id=comment.personality_id).comments) == 1:  # type: ignore
        crud.personality.remove(db=db, id=comment.personality_id)  # type: ignore
    return crud.comment.remove(db=db, id=id)
