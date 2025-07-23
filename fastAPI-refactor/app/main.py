from fastapi import FastAPI
from app.api.router import router as api_router

app = FastAPI()

# Include main API router
app.include_router(api_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI km project!"}
