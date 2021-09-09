from typing import Any, List, Dict

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
    input: List[Dict] = None,
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
        print(i)
        print(fluff[i])
        print(fluff[i]['name'])
        print(fluff[i]['link'])
        tab.append(fluff[i]['name'] + '|' + fluff[i]['link'])
    comment_in['fluff'] = '~'.join(tab)
    comment = crud.comment.create_new_comment(db=db, obj_in=comment_in)
    return comment
