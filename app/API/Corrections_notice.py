from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.Dependancy import get_cur_user
from app.models.Drivers import Drivers
from app.models.Corrections_notice import Corrections_notice
from app.schemas.Corrections_notice import CorrectionsNoticeBase, CorrectionsNotice
from app.crud.Corrections_notice import create_correction_notice, get_violations_by_license, delete_correction_notice

router = APIRouter()

# API endpoint to log a new correction notice | requires an euthenticated officer account
@router.post("/violations/log-notice", response_model=CorrectionsNotice)
def log_corrections_notice(notice_in: CorrectionsNoticeBase, db: Session = Depends(get_db), current_user = Depends(get_cur_user)):
    # Verifies the user is an officer before allowing a notice to be logged
    if not current_user.OfficerID:
        raise HTTPException(status_code=400, detail="No Officer ID linked to account | Incorrect OfficerID used to create Log" )
    
    # Ensures the target drivers license actually exists in the database
    driver = db.query(Drivers).filter(Drivers.DriverLicense == notice_in.DriversLicense).first()
    if not driver:
        raise HTTPException(status_code=404, detail="No driver with this license found in database")
    return create_correction_notice(db, notice_in)

# API endpoint for a logged in driver to retrieve their violation records 
@router.get("/violations/my-violations")
def get_my_violations( db: Session = Depends(get_db), current_user = Depends(get_cur_user)):
    # Restricts access to users who have a drivers license linked to their account
    if not current_user.drivers_license:
        raise HTTPException(status_code=400, detail="No Drivers License links to your account")
    return get_violations_by_license(db, current_user.drivers_license)

# API endpoint for officers to retrieve all correction notices
@router.get("/corrections/all", response_model=list[CorrectionsNotice])
def get_all_corrections(db: Session = Depends(get_db), current_user = Depends(get_cur_user)):
    # Restrict to officers only
    if not current_user.OfficerID:
        raise HTTPException(status_code=403, detail="Officer access required")
    return db.query(Corrections_notice).all()

# API endpoint for an officer to delete a notice by its noticeID
@router.delete("/corrections/delete-notice/{notice_id}")
def delete_notice(notice_id: int, db: Session = Depends(get_db), current_user = Depends(get_cur_user)):
    # Restricts eletion to authenticated officers
    if not current_user.OfficerID:
        raise HTTPException(status_code=400, detail="No OfficerId linked to account")
    
    notice = delete_correction_notice(db, notice_id)
    if not notice:
        raise HTTPException(status_code=404, detail="Notice not found")
    return {"detail": "Notice deleted Successfully"}