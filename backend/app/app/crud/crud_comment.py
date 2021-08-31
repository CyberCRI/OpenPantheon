from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.comment import Comment
from app.schemas.comment import CommentCreate, CommentUpdate


class CRUDComment(CRUDBase[Comment, CommentCreate, CommentUpdate]):
    def create_new_comment(
        self, db: Session, *, obj_in: CommentCreate
    ) -> Comment:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    # def get_multi_by_owner(
    #     self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    # ) -> List[Comment]:
    #     return (
    #         db.query(self.model)
    #         .filter(Comment.owner_id == owner_id)
    #         .offset(skip)
    #         .limit(limit)
    #         .all()
    #     )


comment = CRUDComment(Comment)
