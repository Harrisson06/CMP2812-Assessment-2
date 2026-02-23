from sqlalchemy import Column, Integer, String, Date
from app.db.base import Base

class Drivers(Base):
    __tablename__ = "Drivers"
    First_name = Column(String(20))
    Last_name = Column(String(20))
    Address = Column(String(50))
    City = Column(String(30))
    State = Column(String(20))
    Zipcode = Column(String(5))
    DriverLicense = Column(Integer, primary_key=True)
    State_issued_license = Column(String(15))
    Birthdate = Column(Date)
    Height = Column(Integer)
    Weight = Column(Integer)
    Eyecolour = Column(String(20))