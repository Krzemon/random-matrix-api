from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.compute import router

app = FastAPI(
    title="Random Matrix Api",
    version="0.1.0",
    description="API for calculations on random matrices"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # lub np. ["https://twoja-domena.pl"]
    # allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(api_router, prefix="/api")
app.include_router(router, prefix="/mp")

@app.get("/")
def root():
    return {"message": "EigenFlow API działa"}