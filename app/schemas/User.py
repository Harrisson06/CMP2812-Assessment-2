from pydantic import BaseModel, Field
from typing import Optional

# Base schema for the User table
class UserBase(BaseModel):
    email: str

# Schema for creating user table
class UserCreate(UserBase):
    password: str
    role: Optional[str] = "Citizen"
    OfficerID: Optional[int] = Field(default=None, nullable=True)
    DriversLicense: Optional[int] = None

# Full schema for User, allows orm mapping from the db models. 
class User(UserBase):
    id: int
    role: str
    DriversLicense: Optional[int] = None

    class Config:
        from_attributes = True