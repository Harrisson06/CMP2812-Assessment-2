from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Officers(Base):
    __tablename__ = "Officers"
    OfficerID = Column(Integer, primary_key=True, autoincrement=True)
    First_name = Column(String(30))
    Last_name = Column(String(30))
    Perssonel_nunber = Column(Integer, unique=True)