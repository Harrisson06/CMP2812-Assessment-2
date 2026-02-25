from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.User import User, UserCreate
from app.crud import User as Crud_user

router = APIRouter(prefix="/Users", tags=["Users"])

# API endpoint to register a new user | Checks for existing email and returns 201 on success
@router.post("/", status_code=201, response_model=User)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    # Verifies if the email is already registered in the database
    existing = Crud_user.get_user_by_email(db, user_in.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already in use")
    
    # Creates the user if the email is unique 
    return Crud_user.create_user(db, user_in)

