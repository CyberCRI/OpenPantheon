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
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .comment import Comment  # noqa: F401
    from .personality import Personality  # noqa: F401

personal_pantheon = Table('personal', Base.metadata, Column('user_id', ForeignKey('user.id'), primary_key=True),
                          Column('personality_id', ForeignKey('personality.id'), primary_key=True))


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    job = Column(String, index=True)
    organization = Column(String, index=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    comments = relationship("Comment", backref="user")
    personalities_celebrated = relationship("Personality", secondary=personal_pantheon, backref="users", uselist=True)
