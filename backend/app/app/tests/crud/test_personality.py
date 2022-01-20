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
from sqlalchemy.orm import Session

from app import crud
from app.schemas.personality import PersonalityCreate, PersonalityUpdate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string


def test_create_personality(db: Session) -> None:
    field = random_lower_string()
    gender = random_lower_string()
    personality_in = PersonalityCreate(field=field, gender=gender)
    personality = crud.personality.create_new_personality(db=db, obj_in=personality_in)
    assert personality.field == field
    assert personality.gender == gender


def test_get_personality(db: Session) -> None:
    field = random_lower_string()
    gender = random_lower_string()
    personality_in = PersonalityCreate(field=field, gender=gender)
    personality = crud.personality.create_new_personality(db=db, obj_in=personality_in)
    stored_personality = crud.personality.get(db=db, id=personality.id)
    assert stored_personality
    assert personality.id == stored_personality.id
    assert personality.field == stored_personality.field
    assert personality.gender == stored_personality.gender


def test_update_personality(db: Session) -> None:
    field = random_lower_string()
    gender = random_lower_string()
    personality_in = PersonalityCreate(field=field, gender=gender)
    personality = crud.personality.create_new_personality(db=db, obj_in=personality_in)
    gender2 = random_lower_string()
    personality_update = PersonalityUpdate(gender=gender2)
    personality2 = crud.personality.update(db=db, db_obj=personality, obj_in=personality_update)
    assert personality.id == personality2.id
    assert personality.field == personality2.field
    assert personality2.gender == gender2


def test_delete_personality(db: Session) -> None:
    field = random_lower_string()
    gender = random_lower_string()
    personality_in = PersonalityCreate(field=field, gender=gender)
    personality = crud.personality.create_new_personality(db=db, obj_in=personality_in)
    personality2 = crud.personality.remove(db=db, id=personality.id)
    personality3 = crud.personality.get(db=db, id=personality.id)
    assert personality3 is None
    assert personality2.id == personality.id
    assert personality2.field == field
    assert personality2.gender == gender
