from pydantic import BaseModel
from typing import Optional

class DriversBase(BaseModel):
    First_name: Optional[str] = None
    Last_name: Optional[str] = None
    Address: Optional[str] = None
    City: Optional[str] = None
    State: Optional[str] = None
    ZipCode: Optional[str] = None
    State_issued_license: Optional[str] = None
    Birthdate: Optional[str] = None
    Height: Optional[int] = None
    Weight: Optional[int] = None
    Eyecolour: Optional[str] = None

class Drivers(DriversBase):
    Drivers_license: int 
    class config:
        orm_mode = True