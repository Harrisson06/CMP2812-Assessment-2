from pydantic import BaseModel
from typing import Optional
from datetime import date

# Base schema for the Drivers table
class DriversBase(BaseModel):
    First_name: Optional[str] = None
    Last_name: Optional[str] = None
    Address: Optional[str] = None
    City: Optional[str] = None
    State: Optional[str] = None
    ZipCode: Optional[str] = None
    State_issued_license: Optional[str] = None
    Birthdate: Optional[date] = None
    Height: Optional[int] = None
    Weight: Optional[int] = None
    Eyecolour: Optional[str] = None

# Full schema for Drivers, allows orm mapping from the db models. 
class Drivers(DriversBase):
    DriverLicense: int 
    class Config:
        from_attributes = True