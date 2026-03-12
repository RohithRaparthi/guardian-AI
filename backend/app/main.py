from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.api_router import api_router
from app.database.init_db import init_db

# ----------------------------------------
# CREATE FASTAPI APP
# ----------------------------------------

app = FastAPI(
    title="Fall Detection API",
    version="1.0.0"
)

# ----------------------------------------
# CORS CONFIGURATION
# ----------------------------------------
# Allows React frontend to communicate with backend
# Supports both 5173 and 5174 ports

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------------------
# INITIALIZE DATABASE
# ----------------------------------------

init_db()

# ----------------------------------------
# INCLUDE API ROUTES
# ----------------------------------------

app.include_router(api_router, prefix="/api")

# ----------------------------------------
# ROOT ENDPOINT
# ----------------------------------------

@app.get("/")
def root():
    return {"message": "API Running Successfully"}