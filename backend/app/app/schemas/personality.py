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
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from app.schemas.comment import Comment, CommentFull


# Shared properties
class PersonalityBase(BaseModel):
    field: Optional[str] = None
    continent: Optional[str] = None
    gender: Optional[str] = None
    time_created: Optional[datetime] = None


# Properties to receive on personality creation
class PersonalityCreate(PersonalityBase):
    wikipedia_id: Optional[str]


# Properties to receive on personality update
class PersonalityUpdate(PersonalityBase):
    pass


# Properties shared by models stored in DB
class PersonalityInDBBase(PersonalityBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Personality(PersonalityInDBBase):
    id: int
    wikipedia_id: Optional[str]
    comments: List[Comment] = []
    time_created: Optional[datetime] = None


# Properties to return to client
class PersonalityFull(PersonalityInDBBase):
    id: int
    wikipedia_id: Optional[str]
    comments: List[CommentFull] = []
    time_created: Optional[datetime] = None


# Properties properties stored in DB
class PersonalityInDB(PersonalityInDBBase):
    pass
