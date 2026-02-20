from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Corrections_notice(Base):
    NoticeID = Column(Integer, autoincrement=True, primary_key=True)
    Drivers_license = Column(Integer)
    NoticeIssueDate = Column(String(10))
    District = Column(String(20))
    Location = Column(String(40))
    Violation_time = Column(String(15))
    Violation_desc = Column(String(255))
    OfficerID = Column(Integer)
