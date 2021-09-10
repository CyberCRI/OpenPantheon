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
