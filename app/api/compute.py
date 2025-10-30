from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ComputeRequest(BaseModel):
    x: float
    y: float

class ComputeResponse(BaseModel):
    result: float

@router.post("/compute", response_model=ComputeResponse)
def compute(data: ComputeRequest):
    return ComputeResponse(result=data.x + data.y)