from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.auth import Token
from app.crud import User as CRUD_user
from app.core.security import verify_password, create_access_token

router = APIRouter(tags=["Authenticate"])

# API endpoint to authenticate users and issue JWT access tokens
@router.post("/Login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Look up user by emial or OfficerID provided in the login form
    user = CRUD_user.get_user_email_or_id(db, form_data.username)

    # Validates user and checks the hashed password
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password or email address",
            headers={"WWW-Authenticate": "Bearer"}
        )
    # Generates a fresh token for the authenticated session
    token = create_access_token(subject=user.email)
    return {"access_token": token, "token_type": "Bearer"}