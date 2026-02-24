from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base

# Users table so you can create a username and password to access the database
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(200), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(20), nullable=False, default="Citizen")
    OfficerID = Column(Integer, ForeignKey("Officers.OfficerID"), nullable=True)
    drivers_license = Column(Integer)