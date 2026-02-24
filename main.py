from itertools import product
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List, Optional

from app.API.Corrections_notice import router as Corrections_router 
from app.API.User import router as User_router
from app.API.Auth import router as Auth_router
from app.db.init_db import init_db

app = FastAPI()

init_db()

app.include_router(Corrections_router, prefix="/api", tags=["Corrections"])
app.include_router(User_router, prefix="/api", tags=["Users"])
app.include_router(Auth_router, prefix="/api", tags=["Authenticate"])