from typing import Optional
from fastapi import FastAPI, Body
# import sys
# from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware

# from app.api.config import install_github_package

# from .marchenko_pastur import multiply_matrices, generate_random_matrix

# from pydantic import BaseModel
# import httpx # zewnętrzne serwisy API

app = FastAPI()

# ustawienie folderu libs w sys.path
# libs_path = Path(__file__).parent / "libs"
# sys.path.append(str(libs_path))

# -----------------------------
# Instalacja pakietu z GitHub przy starcie
# -----------------------------
# GITHUB_REPO = "https://github.com/Krzemon/mp-package.git"
# TARGET_DIR = "app/libs"

# try:
#     install_github_package(GITHUB_REPO, TARGET_DIR)
# except Exception as e:
#     print("Błąd instalacji pakietu z GitHub:", e)


# korzystanie z pydantic ?? możnma dataclasses - wbudowane
# class User(BaseModel):
#     name: str
#     email: str
#     id: int

# ----------------------------
# Konfiguracja CORS
# ----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # lub np. ["https://twoja-nazwa.github.io"]
    allow_methods=["*"],
    allow_headers=["*"]
)

# ----------------------------
# Endpointy
# ----------------------------
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/compute")
async def compute():
    # tutaj wywołujesz funkcje z pakietu numba
    result = {"message": "Wynik obliczeń"}  
    return result

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/matrix/random")
async def random_matrix(rows: int = 3, cols: int = 3):
    matrix = generate_random_matrix(rows, cols)
    return {"matrix": matrix.tolist()}  # JSON nie obsługuje ndarray

@app.post("/matrix/multiply")
async def multiply_matrices_endpoint(a: list = Body(...), b: list = Body(...)):
    """
    Otrzymuje dwie macierze w formie list (JSON), mnoży je i zwraca wynik
    """
    import numpy as np

    a_np = np.array(a)
    b_np = np.array(b)
    result = multiply_matrices(a_np, b_np)
    return {"result": result.tolist()}  

# @app.get("/joke")
# async def get_joke():
#     """
#     Pobiera losowy dowcip z zewnętrznego API i zwraca go klientowi
#     """
#     url = "https://official-joke-api.appspot.com/random_joke"
#     async with httpx.AsyncClient() as client:
#         response = await client.get(url)
#         data = response.json()
#     return {"joke": data}