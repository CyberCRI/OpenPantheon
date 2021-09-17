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
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()

# @router.get("/", response_model=List[schemas.Comment])
# def read_comments(
#     db: Session = Depends(deps.get_db),
#     skip: int = 0,
#     limit: int = 100,
#     # current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Retrieve comments.
#     """
#     # if crud.user.is_superuser(current_user):
#     comments = crud.comment.get_multi(db, skip=skip, limit=limit)
#     # else:
#     #     comments = crud.comment.get_multi_by_owner(
#     #         db=db, owner_id=current_user.id, skip=skip, limit=limit
#     #     )
#     return comments


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
    comment_in = input[0]
    del input[0]
    fluff = input
    tab = []
    for i in range(len(fluff)):
        tab.append(fluff[i]['name'] + '|' + fluff[i]['link'])
    comment_in['fluff'] = '~'.join(tab)
    return crud.comment.create_new_comment(db=db, obj_in=comment_in)


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
    if not current_user.id == comment.author_id and not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    crud.user.remove_personality(db=db,
                                 db_obj=crud.user.get(db=db, id=comment.author_id),
                                 id_personality=comment.personality_id)
    if len(crud.personality.get(db=db, id=comment.personality_id).comments) == 1:
        crud.personality.remove(db=db, id=comment.personality_id)
    return crud.comment.remove(db=db, id=id)
