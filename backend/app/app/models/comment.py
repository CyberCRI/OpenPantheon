from typing import TYPE_CHECKING

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base_class import Base

if TYPE_CHECKING:
    from .personality import Personality  # noqa: F401
    from .user import User  # noqa: F401


class Comment(Base):
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    # name = Column(String, index=True)
    fluff = Column(String, index=True)
    # image = Column(String, index=True)
    # job = Column(String, index=True)
    author_id = Column(Integer, ForeignKey("user.id"))
    personality_id = Column(Integer, ForeignKey("personality.id"))
    # owner = relationship("User", back_populates="personalities")
