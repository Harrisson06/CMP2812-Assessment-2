from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker, session

# SQL access point link
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:computing@127.0.0.1:3306/NYSPD"

# Creating the database engine using the above URL
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

# Creating a session to be used to access the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db: session = SessionLocal() # Opens the new session
    try:
        yield db                 # Provides a session to the endpoint
    finally:
        db.close()               # Closes the session after its done