from datetime import datetime, timedelta
from jose import jwt
from werkzeug.security import generate_password_hash, check_password_hash

SECRET_KEY = "my_super_secret_key_12345"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# Hash Password
def hash_password(password: str):
    return generate_password_hash(password)


# Verify Password
def verify_password(password: str, hashed_password: str):
    return check_password_hash(hashed_password, password)


# Create JWT Token
def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )