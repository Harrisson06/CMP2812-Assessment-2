from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Officers(Base):
    __tablename__ = "Officers"
    __table_args__ = {"extend_existing": True}
    OfficerID = Column(Integer, primary_key=True, autoincrement=True)
    FirstName = Column(String(30))
    LastName = Column(String(30))
    PerssonelNumber = Column(Integer, unique=True)