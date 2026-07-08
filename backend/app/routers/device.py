from fastapi import APIRouter
from app.schemas.device import DeviceRegister
from app.services.device_service import DeviceService

router = APIRouter(
    prefix="/device",
    tags=["Device"]
)


@router.post("/register")
async def register_device(device: DeviceRegister):
    return await DeviceService.register_device(device)