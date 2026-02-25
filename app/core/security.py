import os
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from jose import jwt
import hashlib
import base64

# Constants and configuration for JWT encryption and password hashing
SECRET_KEY = os.getenv("SECRET_KEY", "FullStack")                       # Secret key used to encrypt the password 
ALGORITHM = "HS256"                                                     # The encryption algorithm im using 
ACCESS_TOKEN_EXPIRE_MINUTES = 30                                        # Expiry time for each Token
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")       # Library context for password hashing


# Performs an initial SHA-256 hash an Base64 encoding on a raw password string
def prehash_password(password: str) -> str:
    return base64.b64encode(
        hashlib.sha256(password.encode('utf-8')).digest()
        ).decode('utf-8')

# Combines pre-hashing with Bcrypt to securely store passwords in the database
def hash_password(password: str) -> str:
    prehashed = prehash_password(password)
    return pwd_context.hash(prehashed)

# Pre-hashes a plain text password and verifies it against a stored Bcrypt hash
def verify_password(plain_password: str, password_hash: str) -> bool:
    return pwd_context.verify(prehash_password(plain_password), password_hash)

# Generates a JWT token containing the user identity and an expiration timestamp 
def create_access_token(subject: str, expires_minutes: int =
    ACCESS_TOKEN_EXPIRE_MINUTES) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=expires_minutes)
    payload = {"sub": subject, "exp": expire}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)