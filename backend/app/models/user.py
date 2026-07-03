from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class User(BaseModel):
    full_name: str
    email: EmailStr
    mobile: str
    aadhaar_number: str
    password: str
    role: str = "user"
    is_verified: bool = False
    created_at: datetime = datetime.utcnow()


class UserInDB(User):
    id: Optional[str] = None