from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.crud.Vehicles import delete_vehicle

router = APIRouter()

# API endpoint to handle vehicle deletion requests via VIN
@router.delete("/vehicles/delete/{vin}")
def remove_vehicle(vin: str, db: Session = Depends(get_db)):
    vehicle = delete_vehicle(db, vin)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return {"detail": "Vehicle deleted successfully"}