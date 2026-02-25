from sqlalchemy.orm import Session
from typing import Optional
from app.models.User import User as UserModel
from app.schemas.User import UserCreate
from app.core.security import hash_password

# Finds a user in the database using their email
def get_user_by_email(db: Session, email: str) -> Optional[UserModel]:
    # Filters stored emails for the one being used
    return db.query(UserModel).filter(UserModel.email == email).first()

# Finds a user via their OfficerID or email
def get_user_email_or_id(db: Session, identifier: str) -> Optional[UserModel]:
    try: 
        officer_id = int(identifier)
        if officer_id == 0:
            officer_id = None
    except ValueError:
        officer_id = None
    # Checks if the identifier matches the email or the OfficerID
    if officer_id is not None:
        return db.query(UserModel).filter(UserModel.OfficerID == officer_id).first()
    return db.query(UserModel).filter(UserModel.email == identifier).first()


# Creates a new user and saves them to the database in Users table
def create_user(db: Session, user_in: UserCreate) -> UserModel:
    password_hash = hash_password(user_in.password)
    user = UserModel(
        email=user_in.email,
        password_hash = password_hash,              # Hashes the password before saving it
        role=user_in.role or "user",                # If no role is placed defaults to user rather than a null field or error
        OfficerID=user_in.OfficerID or None,        # Allows an officer to use their ID number instead of their email
        drivers_license = user_in.DriversLicense 
    )

    db.add(user)        # Add's the new user
    db.commit()         # Saves the new user to the database
    db.refresh(user)    # Refreshes the database to get a new ID 
    return user         # Returns the created user