from sqlalchemy import Column, Integer, String, Date
from app.db.base import Base

class Drivers(Base):
    __tablename__ = "Drivers"
    FirstName = Column(String(20))
    LastName = Column(String(20))
    Address = Column(String(50))
    City = Column(String(30))
    State = Column(String(20))
    Zipcode = Column(String(5))
    DriverLicense = Column(Integer, primary_key=True)
    StateIssuedLicense = Column(String(15))
    Birthdate = Column(Date)
    HeightInCm = Column(Integer)
    Weight = Column(Integer)
    Eyecolour = Column(String(20))