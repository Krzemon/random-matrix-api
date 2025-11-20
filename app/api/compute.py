# from fastapi import APIRouter, Form
# from fastapi.responses import JSONResponse
# import numpy as np
# import time
# from tqdm import tqdm
# from mp_package.marchenko_pastur import theoretical_eigenvalue_distribution, generate_eigenvalues_batch

# router = APIRouter()

# @router.post("/plot")
# def generate_plot(
#     N1: int = Form(...),
#     N2: int = Form(...),
#     T: int = Form(...),
#     sigma1_squared: float = Form(...),
#     sigma2_squared: float = Form(...),
#     num_trials: int = Form(...),
#     bins: int = Form(...)
# ):
#     N = N1 + N2
#     sigmas_squared = [sigma1_squared, sigma2_squared]
#     batch_size = 10000  # można dodać jako parametr wejściowy
#     x_theo, rho_theo = theoretical_eigenvalue_distribution(
#         N, T, N1, sigmas_squared, num_points=1000
#     )

#     if len(x_theo) == 0 or len(rho_theo) == 0:
#         return JSONResponse({"error": "Nie udało się obliczyć teoretycznego rozkładu."}, status_code=500)

#     all_eigenvalues = []
#     num_batches = num_trials // batch_size
#     start_time = time.time()

#     for i in tqdm(range(num_batches), desc=f"T={T}"):
#         batch_eigenvalues = generate_eigenvalues_batch(N, T, N1, sigmas_squared, batch_size)
#         all_eigenvalues.extend(batch_eigenvalues)

#     elapsed_time = (time.time() - start_time) / 60

#     counts, edges = np.histogram(all_eigenvalues, bins=bins, density=True)
#     centers = (edges[:-1] + edges[1:]) / 2

#     stats = {
#         "mean": float(np.mean(all_eigenvalues)),
#         "var": float(np.var(all_eigenvalues)),
#         "min": float(np.min(all_eigenvalues)),
#         "max": float(np.max(all_eigenvalues)),
#         "elapsed_minutes": float(elapsed_time),
#         "N": N,
#         "r": float(N / T)
#     }

#     chart_data = {
#         "x_hist": centers.tolist(),
#         "y_hist": counts.tolist(),
#         "x_theory": x_theo.tolist(),
#         "y_theory": rho_theo.tolist(),
#         "stats": stats
#     }

#     return JSONResponse(chart_data)


from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
import numpy as np
import time
from tqdm import tqdm
from mp_package.marchenko_pastur import theoretical_eigenvalue_distribution, generate_eigenvalues_batch

router = APIRouter()

@router.post("/plot")
def generate_plot(
    N_list: list[int] = Form(...),
    sigma_squared_list: list[float] = Form(...),
    T: int = Form(...),
    num_trials: int = Form(...),
    bins: int = Form(...)
):
    # N = sum(N_list)
    batch_size = 10000  # można dodać jako parametr wejściowy
    # x_theo, rho_theo = theoretical_eigenvalue_distribution(
    #     N, T, N1, sigma_squared_list, num_points=1000
    # )
    x_theo, rho_theo = theoretical_eigenvalue_distribution(N_list, T, sigma_squared_list, num_points=1000)





    if len(x_theo) == 0 or len(rho_theo) == 0:
        return JSONResponse({"error": "Nie udało się obliczyć teoretycznego rozkładu."}, status_code=500)

    all_eigenvalues = []
    num_batches = num_trials // batch_size
    start_time = time.time()

    for i in tqdm(range(num_batches), desc=f"T={T}"):
        batch_eigenvalues = generate_eigenvalues_batch(N_list, T, sigma_squared_list, batch_size)
        all_eigenvalues.extend(batch_eigenvalues)

    elapsed_time = (time.time() - start_time) / 60

    counts, edges = np.histogram(all_eigenvalues, bins=bins, density=True)
    centers = (edges[:-1] + edges[1:]) / 2

    stats = {
        "mean": float(np.mean(all_eigenvalues)),
        "var": float(np.var(all_eigenvalues)),
        "min": float(np.min(all_eigenvalues)),
        "max": float(np.max(all_eigenvalues)),
        "elapsed_minutes": float(elapsed_time),
        "N": N,
        "r": float(N / T)
    }

    chart_data = {
        "x_hist": centers.tolist(),
        "y_hist": counts.tolist(),
        "x_theory": x_theo.tolist(),
        "y_theory": rho_theo.tolist(),
        "stats": stats
    }

    return JSONResponse(chart_data)