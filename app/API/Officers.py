from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from typing import List

from app.schemas.Officers import Officers
from app.core.Dependancy import get_cur_user
from app.crud.Officers import get_officer_by_license
from app.crud.Officers import get_officers
from app.crud.Officers import update_officer_lastname as crud_update_officer_lastname

router = APIRouter()

@router.get("/officers/linked-to-license/{driversLicense}", response_model=Officers)
def read_officer_by_license(driversLicense: int, db: Session = Depends(get_db)):
    officer = get_officer_by_license(db, driversLicense)
    if not officer:
        # Raises a error code if there is no officer or license number in the database
        raise HTTPException(status_code=404, detail="No officer linked to this License")
    return officer

@router.get("/Officers", response_model=List[Officers])
def read_officers(db: Session = Depends(get_db)):
    return get_officers(db)

@router.put("/officers/update-lastname")
def update_officer_lastname(new_lastname: str, db: Session = Depends(get_db), current_user = Depends(get_cur_user)):
    if not current_user.OfficerID:
        raise HTTPException(status_code=400, detail="No Officer ID linked to your account")
    officer = crud_update_officer_lastname(db, current_user.OfficerID, new_lastname)
    if not officer:
        raise HTTPException(status_code=404, detail="Officer not found")
    return officer