from typing import List, Optional

from pydantic import BaseModel, EmailStr

from app.schemas.personality import Personality


# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    organization: Optional[str] = None
    job: Optional[str] = None
    personalities_celebrated: List[Personality] = []


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    job: Optional[str]
    organization: Optional[str]


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    personalities_celebrated: List[Personality] = []
    job: Optional[str] = None
    organization: Optional[str] = None


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
