from fastapi import APIRouter
from typing import List
from fastapi.responses import JSONResponse
import numpy as np
import time
from tqdm import tqdm
from pydantic import BaseModel

from mp_package.gen_theory import theoretical_eigenvalue_distribution
from mp_package.gen_histogram import generate_eigenvalues

router = APIRouter()

class PlotData(BaseModel):
    N_list: List[int]
    sigma_squared_list: List[float]
    T: int
    num_trials: int
    dist_name: str
    bins: int

@router.post("/plot")
def generate_plot(plot_data: PlotData):
    N_list = plot_data.N_list
    sigma_squared_list = plot_data.sigma_squared_list
    T = plot_data.T
    num_trials = plot_data.num_trials
    dist_name = plot_data.dist_name
    bins = plot_data.bins

    # ------------  Teoretyczny  -------------
    start_time_theo = time.time()
    x_theo, rho_theo, theo_stats = theoretical_eigenvalue_distribution(N_list, T, sigma_squared_list, num_points=1000)
    elapsed_time_theo = (time.time() - start_time_theo) # in seconds
    if not np.isfinite(list(theo_stats.values())).all():
        return JSONResponse({"error": "Statystyki teoretycznego rozkładu zawierają NaN lub inf."}, status_code=400)
    if len(x_theo) == 0 or len(rho_theo) == 0:
        return JSONResponse({"error": "Nie udało się obliczyć teoretycznego rozkładu."}, status_code=500)
    
    # ------------  Histogram  -------------
    start_time_hist = time.time()
    all_eigenvalues, hist_stats = generate_eigenvalues(N_list, T, sigma_squared_list, num_trials, dist_name)
    elapsed_time_hist = (time.time() - start_time_hist) # in seconds
    if not np.isfinite(list(hist_stats.values())).all():
        return JSONResponse({"error": "Statystyki histogramu zawierają NaN lub inf."}, status_code=400)
    if len(all_eigenvalues) == 0:
        return JSONResponse({"error": "Nie udało się obliczyć histogramu."}, status_code=500)

    # ------------  -------------  -------------
    other_stats = {
        "N_total": int(np.sum(N_list)),
        "r": float(np.sum(N_list) / T),
        "time": float(elapsed_time_theo + elapsed_time_hist)
    }

    counts, edges = np.histogram(all_eigenvalues, bins=bins, density=True)
    centers = (edges[:-1] + edges[1:]) / 2
    chart_data = {
        "x_hist": centers.tolist(),
        "y_hist": counts.tolist(),
        "x_theory": x_theo.tolist(),
        "y_theory": rho_theo.tolist(),
        "hist_stats": hist_stats,
        "theo_stats": theo_stats,
        "other_stats": other_stats
    }

    return JSONResponse(chart_data)