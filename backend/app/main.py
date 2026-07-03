from fastapi import FastAPI
from app.routers.auth import router as auth_router

app = FastAPI(
    title="Aadhaar Device Security System",
    version="1.0.0"
)

# Include Authentication Routes
app.include_router(auth_router)


@app.get("/")
async def home():
    return {
        "message": "Aadhaar Device Security System API"
    }