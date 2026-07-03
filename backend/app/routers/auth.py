from fastapi import APIRouter
from app.schemas.user import UserRegister
from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
async def register(user: UserRegister):

    result = await AuthService.register_user(user)

    return result