import time
import numpy as np
from vectors import dot_product

# Generate 1,000 random vectors, each with 512 dimensions
num_vectors = 1000
dim = 512

# 1. Pure Python Lists
python_data = [[float(i) for i in range(dim)] for _ in range(num_vectors)]

# 2. NumPy 2D Array (Matrix)
numpy_data = np.array(python_data)

# --- Timing Pure Python Loop ---
start_time = time.time()
python_results = []
for i in range(num_vectors - 1):
    # Dot product between adjacent vectors
    res = dot_product(python_data[i], python_data[i + 1])
    python_results.append(res)
python_duration = time.time() - start_time

# --- Timing NumPy Vectorized Operation ---
start_time = time.time()
# Matrix multiplication of NumPy arrays: calculates dot products across all rows at once
numpy_results = np.sum(numpy_data[:-1] * numpy_data[1:], axis=1)
numpy_duration = time.time() - start_time

print(f"Pure Python Loop Time: {python_duration:.6f} seconds")
print(f"NumPy Vectorized Time: {numpy_duration:.6f} seconds")
print(f"Speedup Factor: {python_duration / numpy_duration:.2f}x faster")
