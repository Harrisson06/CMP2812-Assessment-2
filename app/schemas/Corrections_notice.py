from pydantic import BaseModel
from typing import Optional

# Base schema for the Corrections_notice table, defining the primary keys
class CorrectionsNoticeBase(BaseModel):
    Drivers_license: Optional[int] = None
    Notice_issue_date: Optional[str] = None
    District: Optional[str] = None
    Location: Optional[str] = None
    Violation_time: Optional[str] = None
    Violation_desc: Optional[str] = None
    Detachment: Optional[str] = None
    OfficerID: Optional[str] = None

# Full schema for Corrections_notice, allows orm mapping from the db models. 
class CorrectionsNotice(CorrectionsNoticeBase):
    NoticeID: int
    class config:
        from_attributes = True