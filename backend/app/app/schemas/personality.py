from typing import Optional, List

from datetime import datetime
from sqlalchemy.dialects.postgresql import JSON

from pydantic import BaseModel

from app.schemas.comment import Comment, CommentFull


# Shared properties
class PersonalityBase(BaseModel):
    field: Optional[str] = None
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
    comments: List[Comment] = None
    time_created: Optional[datetime] = None

# Properties to return to client
class PersonalityFull(PersonalityInDBBase):
    id: int
    wikipedia_id: Optional[str]
    comments: List[CommentFull] = None
    time_created: Optional[datetime] = None


# Properties properties stored in DB
class PersonalityInDB(PersonalityInDBBase):
    pass
