from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey
from app.db.base import Base

class Corrections_notice(Base):
    __tablename__ = "CorrectionsNotice"
    NoticeID = Column(Integer, autoincrement=True, primary_key=True)
    DriversLicense = Column(Integer)
    noticeIssueDate = Column(Date)
    District = Column(String(20))
    Location = Column(String(40))
    ViolationTime = Column(Time)
    ViolationDesc = Column(String(255))
    Detachment = Column(String(30))
    OfficerID = Column(Integer, ForeignKey("Officers.OfficerID"))
