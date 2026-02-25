from sqlalchemy.orm import Session
from app.models.Drivers import Drivers
from app.models.Corrections_notice import Corrections_notice

# Updates the drivers last name via drivers license number and saves it to the database
def update_driver_lastname(db: Session, driver_license: int, new_lastname: str):
    driver = db.query(Drivers).filter(Drivers.DriverLicense == driver_license).first()
    if not driver:
        return None
    driver.LastName = new_lastname
    
    db.commit()
    db.refresh(driver)
    return driver

# Finds an driver by drivers license and updates their address in the database
def update_driver_address(db: Session, driver_license: int, new_address: str):
    driver = db.query(Drivers).filter(Drivers.DriverLicense == driver_license).first()
    if not driver:
        return None
    
    driver.Address = new_address
    db.commit()
    db.refresh(driver)
    return driver

# Deletes a driver and all associated correction notices
def delete_driver(db: Session, driver_license: int):
    driver = db.query(Drivers).filter(Drivers.DriverLicense == driver_license).first()
    if not driver:
        return None
    
    # Removes linked notices first to maintain database integrity
    db.query(Corrections_notice).filter(Corrections_notice.DriversLicense == driver_license).delete()
    db.delete(driver)
    db.commit()
    return driver