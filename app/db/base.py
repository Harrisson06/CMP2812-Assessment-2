from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker, session

SQLALCHEMY_DATABASE_URL = "mysql+mysqlclient://root:SEPS@127.0.0.1:3306/NYSPD"

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db: session = SessionLocal()
    try:
        yield db
    finally:
        db.close()