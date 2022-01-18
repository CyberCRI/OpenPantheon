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
from typing import Optional

from pydantic import BaseModel


# Shared properties
class CommentBase(BaseModel):
    text: Optional[str] = None


# Properties to receive on comment creation
class CommentCreate(CommentBase):
    author_id: Optional[int]
    personality_id: Optional[int]


# Properties to receive on comment update
class CommentUpdate(CommentBase):
    pass


# Properties shared by models stored in DB
class CommentInDBBase(CommentBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Comment(CommentInDBBase):
    author_id: Optional[int]
    personality_id: Optional[int]
    is_validated: Optional[bool] = False


class CommentFull(CommentInDBBase):
    author_id: Optional[int]
    personality_id: Optional[int]
    fluff: Optional[str] = None


# Properties properties stored in DB
class CommentInDB(CommentInDBBase):
    pass
