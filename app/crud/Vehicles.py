from sqlalchemy.orm import Session
from app.models.Vehicles import Vehicles

# Deletes a vehicle based on the vin | Note: doesnt need authentication/login
def delete_vehicle(db: Session, vin: str):
    vehicle = db.query(Vehicles).filter(Vehicles.VIN == vin).first()
    if not vehicle:
        return None
    
    db.delete(vehicle)
    db.commit()
    return vehicle