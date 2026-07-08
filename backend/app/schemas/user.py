from pydantic import BaseModel, EmailStr

class UserRegister(BaseModel):
    full_name: str
    email: EmailStr
    mobile: str
    aadhaar_number: str
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str