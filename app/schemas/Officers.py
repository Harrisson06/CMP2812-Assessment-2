from pydantic import BaseModel
from typing import Optional

# Base schema for the Officers table
class OfficersBase(BaseModel):
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    PersonnelNumber: Optional[int] = None

# Full schema for Officers, allows orm mapping from the db models. 
class Officers(OfficersBase):
    OfficerID: int

    class Config:
        from_attributes = True