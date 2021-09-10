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
    # name = Column(String, index=True)
    field = Column(String, index=True)
    # image = Column(String, index=True)
    # job = Column(String, index=True)
    gender = Column(String, index=True)
    # owner_id = Column(Integer, ForeignKey("user.id"))
    comments = relationship("Comment", backref="personality")
    # owner = relationship("User", back_populates="personalities")
