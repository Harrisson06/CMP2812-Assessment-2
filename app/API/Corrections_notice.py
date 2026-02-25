from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.Dependancy import get_cur_user
from app.models.Drivers import Drivers
from app.schemas.Corrections_notice import CorrectionsNoticeBase, CorrectionsNotice
from app.crud.Corrections_notice import create_correction_notice, get_violations_by_license, delete_correction_notice

router = APIRouter()

@router.post("/corrections/log-correction", response_model=CorrectionsNotice)
def log_corrections_notice(notice_in: CorrectionsNoticeBase, db: Session = Depends(get_db), current_user = Depends(get_cur_user)):
    if not current_user.OfficerID:
        raise HTTPException(status_code=400, detail="No Officer ID linked to account | Incorrect OfficerID used to create Log" )
    
    driver = db.query(Drivers).filter(Drivers.DriverLicense == notice_in.DriversLicense).first()
    if not driver:
        raise HTTPException(status_code=404, detail="Driver with this license not found in the datbase")
    
    return create_correction_notice(db, notice_in)

@router.get("/violations/my-violations")
def get_my_violations( db: Session = Depends(get_db), current_user = Depends(get_cur_user)):
    if not current_user.drivers_license:
        raise HTTPException(status_code=400, detail="No Drivers License links to your account")
    return get_violations_by_license(db, current_user.drivers_license)

@router.delete("/corrections/delete-notice/{notice_id}")
def delete_notice(notice_id: int, db: Session = Depends(get_db), current_user = Depends(get_cur_user)):
    if not current_user.OfficerID:
        raise HTTPException(status_code=400, detail="No OfficerId linked to account")
    notice = delete_correction_notice(db, notice_id)
    if not notice:
        raise HTTPException(status_code=404, detail="Notice not found")
    return {"detail": "Notice deleted Successfully"}