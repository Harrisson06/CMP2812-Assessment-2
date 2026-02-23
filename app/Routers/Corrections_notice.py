from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.Corrections_notice import CorrectionNoticeCreate, CorrectionsNotice
from app.CRUD.Corrections_notice import create_correction_notice

router = APIRouter()

@router.post("/corrections", response_model=CorrectionsNotice)
def log_corrections_notice(notice_in: CorrectionNoticeCreate, db: Session = Depends(get_db)):
    return create_correction_notice(db, notice_in)