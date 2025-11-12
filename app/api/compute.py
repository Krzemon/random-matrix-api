from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
import numpy as np

router = APIRouter()

# To podejście jest w pełni poprawne i proste.
# Nie potrzebujesz Pydantic BaseModel, bo nie wysyłasz JSON, tylko dane formularza.
# Kiedy użyć Pydantic:
# Jeśli chcesz wysyłać JSON POST zamiast form-data (fetch(url, {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify(data)})).
# Daje dodatkowe walidacje, wartości domyślne i automatyczne dokumentowanie w Swagger UI.
# W Twoim przypadku, jeśli wszystko działa z Form(...), nie ma potrzeby komplikować kodu Pydanticem.
@router.post("/plot")
def generate_plot(
    N1: int = Form(...),
    N2: int = Form(...),
    T: int = Form(...),
    sigma_squared: float = Form(...),
    num_trials: int = Form(...),
    bins: int = Form(...)
):
    mu_total = 0
    sigma_total = np.sqrt(sigma_squared)

    samples = np.random.normal(mu_total, sigma_total, num_trials)
    counts, edges = np.histogram(samples, bins=bins, density=True)
    centers = (edges[:-1] + edges[1:]) / 2

    theory = (1 / (sigma_total * np.sqrt(2 * np.pi))) * np.exp(
        -0.5 * ((centers - mu_total) / sigma_total) ** 2
    )

    chart_data = {
        "x": centers.tolist(),
        "hist": counts.tolist(),
        "theory": theory.tolist(),
        "stats": {
            "mean": float(np.mean(samples)),
            "var": float(np.var(samples)),
            "min": float(np.min(samples)),
            "max": float(np.max(samples))
        }
    }
    return JSONResponse(chart_data)



# # OLD: RYSUJE GAUSSA ALE DZIALA: ZWRACA HTML
# from fastapi import APIRouter, Form
# from fastapi.responses import HTMLResponse
# import numpy as np
# import json

# router = APIRouter()


# @router.post("/plot", response_class=HTMLResponse)
# def generate_plot(
#     N1: int = Form(...),
#     N2: int = Form(...),
#     T: int = Form(...),
#     sigma_squared: float = Form(...),
#     num_trials: int = Form(...),
#     bins: int = Form(...)
# ):
#     """
#     Endpoint generujący histogram i teoretyczny rozkład Gaussa
#     dla danych parametrów z formularza HTMX.
#     """

#     # --- Obliczenia ---
#     N_total = N1 + N2
#     mu_total = 0
#     sigma_total = np.sqrt(sigma_squared)

#     # Generowanie próbek (symulacja)
#     samples = np.random.normal(loc=mu_total, scale=sigma_total, size=num_trials)

#     # Histogram (gęstość prawdopodobieństwa)
#     counts, edges = np.histogram(samples, bins=bins, density=True)
#     centers = (edges[:-1] + edges[1:]) / 2

#     # Teoretyczny rozkład Gaussa
#     theory = (1 / (sigma_total * np.sqrt(2 * np.pi))) * np.exp(
#         -0.5 * ((centers - mu_total) / sigma_total) ** 2
#     )

#     # Dane dla Chart.js
#     chart_data = {
#         "x": centers.tolist(),
#         "hist": counts.tolist(),
#         "theory": theory.tolist()
#     }

#     # --- Fragment HTML do wstrzyknięcia przez HTMX ---
#     html = f"""
#     <div class="mt-6">
#       <h3 class="text-lg font-semibold mb-2 text-center">
#         Histogram i krzywa teoretyczna (σ² = {sigma_squared})
#       </h3>
#       <canvas id="histogram-chart" 
#               data-chart='{json.dumps(chart_data)}' 
#               width="600" 
#               height="400" 
#               class="mx-auto">
#       </canvas>
#     </div>
#     """
#     return HTMLResponse(html)






# from fastapi import APIRouter
# from models.parameters import PlotParams
# import numpy as np

# router = APIRouter()

# moje macierze

# @router.post("/plot")
# def generate_plot(params: PlotParams):
#     N1, N2, T = params.N1, params.N2, params.T
#     sigmas_squared = params.sigmas_squared
#     num_trials = params.num_trials
#     batch_size = params.batch_size
#     bins = params.bins

#     # --------------------------
#     # Tutaj Twoje obliczenia
#     # --------------------------
#     # Na potrzeby przykładu generujemy dane normalne
#     data = np.random.normal(0, np.sqrt(sigmas_squared[0]), size=num_trials)

#     # Histogram
#     hist, edges = np.histogram(data, bins=bins, density=True)
#     x = (edges[:-1] + edges[1:]) / 2  # środek binów

#     # Krzywa teoretyczna (normalna)
#     sigma = np.sqrt(sigmas_squared[0])
#     theory = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-x**2 / (2 * sigma**2))

#     # Zwracamy JSON
#     return {
#         "x": x.tolist(),
#         "hist": hist.tolist(),
#         "theory": theory.tolist()
#     }