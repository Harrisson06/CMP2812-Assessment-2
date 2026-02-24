import os
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from jose import jwt
import hashlib
import base64


SECRET_KEY = os.getenv("SECRET_KEY", "CHANGE_ME")                   # Secret key used to encrypt the password 
ALGORITHM = "HS256"                                                 # The encryption algorithm im using 
ACCESS_TOKEN_EXPIRE_MINUTES = 30                                    # Expiry time for each Token
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")   # IDK yet


def prehash_password(password: str) -> str:
    return base64.b64encode(
        hashlib.sha256(password.encode('utf-8')).digest()
        ).decode('utf-8')

def hash_password(password: str) -> str:
    prehashed = prehash_password(password)
    print(f"Original length: {len(password)}")
    print(f"Prehashed length: {len(prehashed)}")
    print(f"Prehashed value: {prehashed}")
    print(f"Password length: {len(prehashed)}")
    return pwd_context.hash(prehashed)

def verify_password(plain_password: str, password_hash: str) -> bool:
    return pwd_context.verify(prehash_password(plain_password), password_hash)

def create_access_token(subject: str, expires_minutes: int =
    ACCESS_TOKEN_EXPIRE_MINUTES) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=expires_minutes)
    payload = {"sub": subject, "exp": expire}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)