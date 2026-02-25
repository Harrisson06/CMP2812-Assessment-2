from sqlalchemy.orm import Session
from app.models.Drivers import Drivers
from app.models.Corrections_notice import Corrections_notice

# updates the drivers last name and commits those changes to the database
def update_driver_lastname(db: Session, driver_license: int, new_lastname: str):
    driver = db.query(Drivers).filter(Drivers.DriverLicense == driver_license).first()
    if not driver:
        return None
    driver.LastName = new_lastname
    
    db.commit()
    db.refresh(driver)
    return driver

# updates the drivers address and commits those changes to the database
def update_driver_address(db: Session, driver_license: int, new_address: str):
    driver = db.query(Drivers).filter(Drivers.DriverLicense == driver_license).first()
    if not driver:
        return None
    
    driver.Address = new_address
    db.commit()
    db.refresh(driver)
    return driver

def delete_driver(db: Session, driver_license: int):
    driver = db.query(Drivers).filter(Drivers.DriverLicense == driver_license).first()
    if not driver:
        return None
    
    db.query(Corrections_notice).filter(Corrections_notice.DriversLicense == driver_license).delete()
    db.delete(driver)
    db.commit()
    return driver