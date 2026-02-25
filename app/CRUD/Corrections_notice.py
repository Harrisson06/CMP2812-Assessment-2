from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.Corrections_notice import Corrections_notice as Corrections_notice_model
from app.schemas.Corrections_notice import CorrectionsNoticeBase

def get_corrections_notice(db: Session) -> List[Corrections_notice_model]:
    # Returns all correction notices from the database as a list
    return db.query(Corrections_notice_model).all()

def get_correction_notice(db: Session, NoticeID: int) -> Optional[Corrections_notice_model]:
    # Returns a single notice by its NoticeID | returns none if not found 
    return db.query(Corrections_notice_model).filter(Corrections_notice_model.NoticeID == NoticeID).first()

def get_violations_by_license(db: Session, drivers_license: int):
    # Returns all notices associated with a specific drivers license number
    return db.query(Corrections_notice_model).filter(
        Corrections_notice_model.DriversLicense == drivers_license
    ).all()

# Creates a new correction notice and adds it to the database
def create_correction_notice(db: Session, notice_in: CorrectionsNoticeBase) -> Corrections_notice_model:
    notice = Corrections_notice_model(
        DriversLicense = notice_in.DriversLicense,
        noticeIssueDate = notice_in.noticeIssueDate,
        District = notice_in.District,
        Location = notice_in.Location,
        ViolationTime = notice_in.ViolationTime,
        ViolationDesc = notice_in.ViolationDesc,
        Detachment = notice_in.Detachment,
        OfficerID = notice_in.OfficerID,
    )
    db.add(notice)
    db.commit()
    db.refresh(notice)
    return notice

# Finds a notice by ID and deletes a notice using the notice id | Note: doesnt require authentication/login
def delete_correction_notice(db: Session, notice_id: int):
    notice = db.query(Corrections_notice_model).filter(Corrections_notice_model.NoticeID == notice_id).first()
    if not notice:
        return None
    db.delete(notice)
    db.commit()
    return notice