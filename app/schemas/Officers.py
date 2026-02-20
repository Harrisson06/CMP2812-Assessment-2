from pydantic import BaseModel
from typing import Optional

# # Base schema for the Officers table
class OfficersBase(BaseModel):
    First_name: Optional[str] = None
    Last_name: Optional[str] = None
    Perssonel_nunber: Optional[int] = None

# Full schema for Officers, allows orm mapping from the db models. 
class Officers(OfficersBase):
    OfficerID: int

    class Config:
        from_attributes = True