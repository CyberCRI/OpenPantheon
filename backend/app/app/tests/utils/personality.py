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

from app import crud, models
from app.schemas.personality import PersonalityCreate
from app.tests.utils.utils import random_lower_string


def create_random_personality(db: Session) -> models.Personality:
    name = random_lower_string()
    description = random_lower_string()
    personality_in = PersonalityCreate(name=name, description=description, id=id)
    return crud.personality.create_new_personality(db=db, obj_in=personality_in)
