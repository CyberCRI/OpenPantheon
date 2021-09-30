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
import math
from typing import Dict, Iterable, List, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func

from app.crud.base import CRUDBase
from app.models.comment import Comment
from app.models.personality import Personality
from app.schemas.personality import PersonalityCreate, PersonalityUpdate


class CRUDPersonality(CRUDBase[Personality, PersonalityCreate, PersonalityUpdate]):
    def create_new_personality(self, db: Session, *, obj_in: PersonalityCreate) -> Personality:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_by_wiki(self, db: Session, *, wiki_id: str) -> Optional[Personality]:
        return db.query(Personality).filter(Personality.wikipedia_id == wiki_id).first()

    def get_stats(self, db: Session) -> Dict:
        result = {'count': 0, 'parity': 0}
        result['count'] = db.query(Personality).count()
        if result['count'] > 0:
            result['parity'] = db.query(Personality).filter(Personality.gender == 'f').count()
            result['parity'] = math.floor(result['parity'] / result['count'] * 100)
        return result

    def get_multi_personalities(self,
                                get_count: List[int],
                                db: Session,
                                current_user_pantheon: Iterable[Personality],
                                *,
                                skip: int = 0,
                                limit: int = 100,
                                personal: int = 0,
                                women: bool = False,
                                field: str = '',
                                region: str = '',
                                sort: str = '') -> List[Personality]:
        result = db.query(Personality).join(Comment).group_by(Personality.id)
        if personal:
            result = result.filter(Personality.id.in_([p.id for p in current_user_pantheon]))
        if women:
            result = result.filter(Personality.gender == 'f')
        if field:
            result = result.filter(Personality.field.like(field))
        if region:
            result = result.filter(Personality.continent.like(region))
        if sort:
            if sort == 'recent':
                result = result.order_by(Personality.id.desc())
            elif sort == 'celebrated':
                result = result.order_by(func.count().desc())
            else:
                result = result.order_by(Personality.id)
        get_count.append(result.count())
        return result.offset(skip).limit(limit).all()

    def get_multi_personalities_guest(self,
                                      get_count: List[int],
                                      db: Session,
                                      *,
                                      skip: int = 0,
                                      limit: int = 100,
                                      women: bool = False,
                                      field: str = '',
                                      region: str = '',
                                      sort: str = '') -> List[Personality]:
        result = db.query(Personality).join(Comment).group_by(Personality.id)
        if women:
            result = result.filter(Personality.gender == 'f')
        if field:
            result = result.filter(Personality.field.like(field))
        if region:
            result = result.filter(Personality.continent.like(region))
        if sort:
            if sort == 'recent':
                result = result.order_by(Personality.id.desc())
            elif sort == 'celebrated':
                result = result.order_by(func.count().desc())
            else:
                result = result.order_by(Personality.id)
        get_count.append(result.count())
        return result.offset(skip).limit(limit).all()


personality = CRUDPersonality(Personality)
