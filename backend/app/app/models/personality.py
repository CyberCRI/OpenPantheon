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
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import func

from app.db.base_class import Base

if TYPE_CHECKING:
    from .comment import Comment  # noqa: F401
    from .user import User  # noqa: F401


class Personality(Base):
    id = Column(Integer, primary_key=True, index=True)
    wikipedia_id = Column(String, index=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    field = Column(String, index=True)
    continent = Column(String, index=True)
    gender = Column(String, index=True)
    comments = relationship("Comment", backref="personality")
