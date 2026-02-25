from sqlalchemy.orm import Session
from app.models.Drivers import Drivers

def update_driver_lastname(db: Session, driver_license: int, new_lastname: str):
    driver = db.query(Drivers).filter(Drivers.DriverLicense == driver_license).first()
    if not driver:
        return None
    driver.LastName = new_lastname
    
    db.commit()
    db.refresh(driver)
    return driver