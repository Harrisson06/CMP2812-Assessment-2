from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Vehicles(Base):
    __tablename__ = "Vehicles"
    DriversLicense = Column(Integer)
    Colour = Column(String(12))
    Make = Column(String(20))
    VIN = Column(String(17), primary_key=True)
    LicensePlate = Column(String(8))
    RegisteredAddress = Column(String(20))
    StateRegistered = Column(String(20))
    RegisteredYear = Column(Integer)
    CarType = Column(String(20))