from pydantic import BaseModel
from typing import Optional

# Base schema for the Vehicles table
class VehiclesBase(BaseModel):
    DriversLicense: Optional[int] = None
    Colour: Optional[str] = None
    Make: Optional[str] = None
    LicensePlate: Optional[str] = None
    RegisteredAddress: Optional[str] = None
    StateRegistered: Optional[str] = None
    RegisteredYear: Optional[int] = None
    CarType: Optional[str] = None

# Full schema for Vehicles, allows orm mapping from the db models. 
class Vehicle(VehiclesBase):
    VIN: str
    class Config:
        from_attributes = True