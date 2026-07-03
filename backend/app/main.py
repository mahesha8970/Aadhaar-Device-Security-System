from fastapi import FastAPI

app = FastAPI(title="Aadhaar Device Security System")

@app.get("/")
def home():
    return {"message": "Backend is running successfully"}