from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.Dependancy import get_cur_user
from app.schemas.Corrections_notice import CorrectionsNoticeBase, CorrectionsNotice
from app.CRUD.Corrections_notice import create_correction_notice, get_violations_by_license

router = APIRouter()

@router.post("/corrections/log-correction", response_model=CorrectionsNotice)
def log_corrections_notice(notice_in: CorrectionsNoticeBase, db: Session = Depends(get_db), current_user = Depends(get_cur_user)):
    if not current_user.OfficerID:
        raise HTTPException(status_code=400, detail="No Officer ID linked to account | Incorrect OfficerID used to create Log" )
    return create_correction_notice(db, notice_in)

@router.get("/violations/my-violations")
def get_my_violations( db: Session = Depends(get_db), current_user = Depends(get_cur_user)):
    if not current_user.DriversLicense:
        raise HTTPException(status_code=400, detail="No Drivers License links to your account")
    return get_violations_by_license(db, current_user.DriversLicense)