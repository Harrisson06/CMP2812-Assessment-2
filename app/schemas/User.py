from pydantic import BaseModel, Field
from typing import Optional

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str
    role: Optional[str] = "Citizen"
    OfficerID: Optional[int] = Field(default=None, nullable=True)

class User(UserBase):
    id: int
    role: str

    class Config:
        from_attributes = True