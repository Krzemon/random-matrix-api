from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.router import api_router

app = FastAPI(
    title="random-matrix-api",
    version="0.1.0",
    description="API for calculations on random matrices"
)

# app.include_router(api_router, prefix="/api")
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # lub np. ["https://twoja-domena.pl"]
    # allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)