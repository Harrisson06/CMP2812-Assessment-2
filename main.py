from fastapi import FastAPI

from app.API.Corrections_notice import router as Corrections_router 
from app.API.User import router as User_router
from app.API.Auth import router as Auth_router
from app.API.Officers import router as Officer_router
from app.API.Drivers import router as Driver_router
from app.API.Vehicles import router as Vehicle_router
from app.db.init_db import init_db

app = FastAPI()

init_db()

app.include_router(Corrections_router, prefix="/api", tags=["Corrections"])
app.include_router(User_router, prefix="/api", tags=["Users"])
app.include_router(Auth_router, prefix="/api", tags=["Authenticate"])
app.include_router(Officer_router, prefix="/api", tags=["Officers"])
app.include_router(Driver_router, prefix="/api", tags=["Drivers"])
app.include_router(Vehicle_router, prefix="/api", tags=["Vehicles"])