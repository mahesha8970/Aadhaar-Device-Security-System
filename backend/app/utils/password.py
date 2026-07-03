from app.config.security import hash_password, verify_password


def get_password_hash(password: str):
    return hash_password(password)


def check_password(plain_password: str, hashed_password: str):
    return verify_password(plain_password, hashed_password)