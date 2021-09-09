from typing import Optional, List, Dict

from sqlalchemy import DateTime
from sqlalchemy.dialects.postgresql import JSON

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

class CommentFull(CommentInDBBase):
    author_id: Optional[int]
    personality_id: Optional[int]
    fluff: Optional[str] = None    

# Properties properties stored in DB
class CommentInDB(CommentInDBBase):
    pass
