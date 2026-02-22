from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.User import UserCreate, User
from app.CRUD.User import create_user, get_user_by_email

router = APIRouter()

@router.post("/Users", response_model=User)

def Register_user(user_in: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, email=user_in.email)
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="A user with this email already exists"
        )
    return create_user(db, user_in)