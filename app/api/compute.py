import io
import base64
import matplotlib.pyplot as plt
from fastapi import APIRouter
from models.parameters import PlotParams

from mp_package import *

router = APIRouter()

@router.post("/plot")
def generate_plot(params: PlotParams):
    N1, N2, T = params.N1, params.N2, params.T
    N = N1 + N2
    sigmas_squared = params.sigmas_squared
    num_trials = params.num_trials
    batch_size = params.batch_size
    bins = params.bins

    # --- tutaj Twoje funkcje obliczeniowe ---
    # np. theoretical_eigenvalue_distribution() i generate_eigenvalues_batch()
    # Dla przykładu wstawiam prosty wykres:

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist([1, 2, 2.5, 3, 3, 3.5, 4], bins=bins, color='skyblue')
    ax.set_title(f"N={N}, T={T}")
    ax.set_xlabel("Wartość własna")
    ax.set_ylabel("Gęstość")

    # --- konwersja do base64 ---
    buf = io.BytesIO()
    plt.tight_layout()
    plt.savefig(buf, format="png", dpi=150)
    plt.close(fig)
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode("utf-8")

    return {"image": f"data:image/png;base64,{image_base64}"}








# from fastapi import APIRouter
# from pydantic import BaseModel

# router = APIRouter()

# class ComputeRequest(BaseModel):
#     x: float
#     y: float

# class ComputeResponse(BaseModel):
#     result: float

# @router.post("/compute", response_model=ComputeResponse)
# def compute(data: ComputeRequest):
#     return ComputeResponse(result=data.x + data.y)








# # ----------------------------
# # Endpointy
# # ----------------------------
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.get("/api/compute")
# async def compute():
#     # tutaj wywołujesz funkcje z pakietu numba
#     result = {"message": "Wynik obliczeń"}  
#     return result

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}

# @app.get("/matrix/random")
# async def random_matrix(rows: int = 3, cols: int = 3):
#     matrix = generate_random_matrix(rows, cols)
#     return {"matrix": matrix.tolist()}  # JSON nie obsługuje ndarray

# @app.post("/matrix/multiply")
# async def multiply_matrices_endpoint(a: list = Body(...), b: list = Body(...)):
#     """
#     Otrzymuje dwie macierze w formie list (JSON), mnoży je i zwraca wynik
#     """
#     import numpy as np

#     a_np = np.array(a)
#     b_np = np.array(b)
#     result = multiply_matrices(a_np, b_np)
#     return {"result": result.tolist()}  


# # import httpx # zewnętrzne serwisy API
# # @app.get("/joke")
# # async def get_joke():
# #     """
# #     Pobiera losowy dowcip z zewnętrznego API i zwraca go klientowi
# #     """
# #     url = "https://official-joke-api.appspot.com/random_joke"
# #     async with httpx.AsyncClient() as client:
# #         response = await client.get(url)
# #         data = response.json()
# #     return {"joke": data}