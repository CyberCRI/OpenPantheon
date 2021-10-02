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
from typing import TYPE_CHECKING

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.sql import func

from app.db.base_class import Base

if TYPE_CHECKING:
    from .personality import Personality  # noqa: F401
    from .user import User  # noqa: F401


class Comment(Base):
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    fluff = Column(String, index=True)
    author_id = Column(Integer, ForeignKey("user.id"))
    personality_id = Column(Integer, ForeignKey("personality.id"))
