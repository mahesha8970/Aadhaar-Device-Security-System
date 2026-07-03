from pydantic import BaseModel, EmailStr, Field


# User Registration Request
class UserRegister(BaseModel):
    full_name: str = Field(..., min_length=3, max_length=100)
    email: EmailStr
    mobile: str = Field(..., min_length=10, max_length=10)
    aadhaar_number: str = Field(..., min_length=12, max_length=12)
    password: str = Field(..., min_length=8)


# User Login Request
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# API Response
class UserResponse(BaseModel):
    message: str