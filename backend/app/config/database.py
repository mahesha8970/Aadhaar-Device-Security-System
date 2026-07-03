import os
from pathlib import Path

from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

# Load .env file from backend folder
BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env")

# Read environment variables
MONGODB_URL = os.getenv("MONGODB_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")

# Check if .env loaded correctly
if not MONGODB_URL:
    raise ValueError("MONGODB_URL is not found in .env")

if not DATABASE_NAME:
    raise ValueError("DATABASE_NAME is not found in .env")

# Create MongoDB client
client = AsyncIOMotorClient(MONGODB_URL)

# Connect to database
database = client[DATABASE_NAME]

# Collections
users_collection = database["users"]
devices_collection = database["devices"]
otp_collection = database["otps"]
security_logs_collection = database["security_logs"]
admins_collection = database["admins"]