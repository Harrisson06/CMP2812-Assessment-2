from pydantic import BaseModel
from typing import Optional

class CorrectionsNoticeBase(BaseModel):
    Drivers_license: Optional[int] = None
    Notice_issue_date: Optional[str] = None
    District: Optional[str] = None
    Location: Optional[str] = None
    Violation_time: Optional[str] = None
    Violation_desc: Optional[str] = None
    Detachment: Optional[str] = None
    OfficerID: Optional[str] = None

class CorrectionsNotice(CorrectionsNoticeBase):
    NoticeID: int
    class config:
        orm_mode = True