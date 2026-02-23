from pydantic import BaseModel
from typing import Optional
from datetime import date, time 

# Base schema for the Corrections_notice table, defining the primary keys
class CorrectionsNoticeBase(BaseModel):
    DriversLicense: Optional[int] = None
    noticeIssueDate: Optional[date] = None
    District: Optional[str] = None
    Location: Optional[str] = None
    ViolationTime: Optional[time] = None
    ViolationDesc: Optional[str] = None
    Detachment: Optional[str] = None
    OfficerID: int 

# Full schema for Corrections_notice, allows orm mapping from the db models. 
class CorrectionsNotice(CorrectionsNoticeBase):
    NoticeID: int
    class config:
        from_attributes = True
