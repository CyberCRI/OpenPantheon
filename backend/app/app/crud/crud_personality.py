from typing import List, Optional, Dict
import math

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func

from app.crud.base import CRUDBase
from app.models.personality import Personality
from app.models.comment import Comment
from app.schemas.personality import PersonalityCreate, PersonalityUpdate


class CRUDPersonality(CRUDBase[Personality, PersonalityCreate, PersonalityUpdate]):
    def create_new_personality(
        self, db: Session, *, obj_in: PersonalityCreate
    ) -> Personality:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_wiki(self, db: Session, *, wiki_id: str) -> Optional[Personality]:
        return db.query(Personality).filter(Personality.wikipedia_id == wiki_id).first()

    def get_stats(
        self, db
    ) -> Dict:
        result = {
            'count': 0,
            'parity': 0
        }
        result['count'] = db.query(Personality).count()
        if result['count'] > 0:
            result['parity'] = db.query(Personality).filter(Personality.gender == 'f').count()
            result['parity'] = math.floor(result['parity'] / result['count'] * 100)
        return result

    def get_multi_personalities(
        self, get_count: List[int], db: Session, current_user_pantheon: List[Personality], *, skip: int = 0, limit: int = 100, personal: int = 0, women: bool = False, field: int = 0, sort: str = ''
    ) -> List[Personality]:
        result = db.query(Personality).join(Comment).group_by(Personality.id)
        if personal:
            result = result.filter(Personality.id.in_([p.id for p in current_user_pantheon]))
        if women:
            result = result.filter(Personality.gender == 'f')
        if sort:
            if sort == 'recent':
                result = result.order_by(Personality.id.desc())
            elif sort == 'celebrated':
                result = result.order_by(func.count().desc())
            else:
                result = result.order_by(Personality.id)
        get_count.append(result.count())
        result = result.offset(skip).limit(limit).all()
        return result

    def get_multi_personalities_guest(
        self, get_count: List[int], db: Session, *, skip: int = 0, limit: int = 100, women: bool = False, field: int = 0, sort: str = ''
    ) -> List[Personality]:
        result = db.query(Personality).join(Comment).group_by(Personality.id)
        if women:
            result = result.filter(Personality.gender == 'f')
        if sort:
            if sort == 'recent':
                result = result.order_by(Personality.id.desc())
            elif sort == 'celebrated':
                result = result.order_by(func.count().desc())
            else:
                result = result.order_by(Personality.id)
        get_count.append(result.count())
        result = result.offset(skip).limit(limit).all()
        return result

    # def get_multi_by_owner(
    #     self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    # ) -> List[Personality]:
    #     return (
    #         db.query(self.model)
    #         .filter(Personality.owner_id == owner_id)
    #         .offset(skip)
    #         .limit(limit)
    #         .all()
    #     )


personality = CRUDPersonality(Personality)
