from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.core.Dependancy import get_cur_user
from app.crud.Drivers import update_driver_lastname, update_driver_address, delete_driver

router = APIRouter()

@router.put("/drivers/update-lastname")
def update_lastname(new_lastname: str, db: Session = Depends(get_db), current_user = Depends(get_cur_user)):
    if not current_user.drivers_license:
        raise HTTPException(status_code=400, detail="No drivers license linked to your account")
    driver = update_driver_lastname(db, current_user.drivers_license, new_lastname)
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    return driver

@router.put("/drivers/update-address")
def update_address(driver_license: int, new_address: str, db: Session = Depends(get_db)):
    driver = update_driver_address(db, driver_license, new_address)
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    return driver

@router.delete("/drivers/delete/{driver_license}")
def remove_driver(driver_license: int, db: Session = Depends(get_db)):
    driver = delete_driver(db, driver_license)
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    return {"detail": "Driver deleted successfully"}
