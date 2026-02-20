from pydantic import BaseModel
from typing import Optional

# Base schema for the Vehicles table
class VehiclesBase(BaseModel):
    Drivers_license: Optional[int] = None
    Colour: Optional[str] = None
    Make: Optional[str] = None
    License_plate: Optional[str] = None
    Registered_address: Optional[str] = None
    State_registered: Optional[str] = None
    Registered_year: Optional[int] = None
    Car_type: Optional[str] = None

# Full schema for Vehicles, allows orm mapping from the db models. 
class Vehicle(VehiclesBase):
    VIN: str
    class Config:
        from_attributes = True