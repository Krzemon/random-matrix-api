from fastapi import APIRouter
from typing import List
from fastapi.responses import JSONResponse
import numpy as np
import time
from tqdm import tqdm
from pydantic import BaseModel

from mp_package.marchenko_pastur import theoretical_eigenvalue_distribution, generate_eigenvalues

router = APIRouter()

class PlotPayload(BaseModel):
    N_list: List[int]
    sigma_squared_list: List[float]
    T: int
    num_trials: int
    bins: int

@router.post("/plot")
def generate_plot(payload: PlotPayload):
    N_list = payload.N_list
    sigma_squared_list = payload.sigma_squared_list
    T = payload.T
    num_trials = payload.num_trials
    bins = payload.bins

    print("DEBUG: N_list:", N_list)
    print("DEBUG: sigma_squared_list:", sigma_squared_list)
    print("DEBUG: T:", T, "num_trials:", num_trials, "bins:", bins)

    # -------------------------
    # Teoretyczny rozkład
    # -------------------------
    x_theo, rho_theo = theoretical_eigenvalue_distribution(N_list, T, sigma_squared_list, num_points=1000)
    if len(x_theo) == 0 or len(rho_theo) == 0:
        return JSONResponse({"error": "Nie udało się obliczyć teoretycznego rozkładu."}, status_code=500)

    # -------------------------
    # Wartości własne
    # -------------------------
    start_time = time.time()
    all_eigenvalues = generate_eigenvalues(N_list, T, sigma_squared_list, num_trials)
    elapsed_time = (time.time() - start_time) # in seconds

    # -------------------------
    # Histogram
    # -------------------------
    counts, edges = np.histogram(all_eigenvalues, bins=bins, density=True)
    centers = (edges[:-1] + edges[1:]) / 2

    # -------------------------
    # Statystyki
    # -------------------------
    stats = {
        "mean": float(np.mean(all_eigenvalues)),
        "var": float(np.var(all_eigenvalues)),
        "min": float(np.min(all_eigenvalues)),
        "max": float(np.max(all_eigenvalues)),
        "elapsed_minutes": float(elapsed_time),
        "N_total": int(np.sum(N_list)),
        "r": float(np.sum(N_list) / T)
    }

    chart_data = {
        "x_hist": centers.tolist(),
        "y_hist": counts.tolist(),
        "x_theory": x_theo.tolist(),
        "y_theory": rho_theo.tolist(),
        "stats": stats
    }

    return JSONResponse(chart_data)