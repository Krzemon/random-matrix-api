import numpy as np
# from numba import njit
from matrix_utils.file1 import *


# @njit
def multiply_matrices(a: np.ndarray, b: np.ndarray):
    """Mnoży dwie macierze"""
    return np.dot(a, b)

def generate_random_matrix(rows: int, cols: int):
    """Generuje losową macierz"""
    return np.random.rand(rows, cols)
# 