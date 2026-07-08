from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Device(BaseModel):
    device_name: str
    brand: str
    model: str
    serial_number: str
    imei: str
    owner_email: str
    is_activated: bool = False
    aadhaar_verified: bool = False
    created_at: datetime = datetime.utcnow()


class DeviceInDB(Device):
    id: Optional[str] = None