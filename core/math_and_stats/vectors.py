import math
import numpy as np

def dot_product(v1: list[float], v2: list[float]) -> float:
    """Calculates the dot product of two equal-length vectors."""
    if len(v1) != len(v2):
        raise ValueError("Vectors must be of identical length.")

    return sum(x * y for x, y in zip(v1, v2))

def vector_magnitude(v: list[float]) -> float:
    """Calculates the Euclidean norm (magnitude) of a vector: ||v|| = sqrt(sum(v_i^2))."""
    return math.sqrt(sum(x ** 2 for x in v))

def cosine_similarity(v1: list[float], v2: list[float]) -> float:
    """Calculates cosine similarity between two vectors."""
    mag1 = vector_magnitude(v1)
    mag2 = vector_magnitude(v2)

    if mag1 == 0.0 or mag2 == 0.0:
        raise ValueError("Cannot calculate cosine similarity for zero vectors.")

    return dot_product(v1, v2) / (mag1 * mag2)

def batch_cosine_similarity(matrix_a: np.ndarray, matrix_b: np.ndarray) -> np.ndarray:
    """
    Computes pairwise cosine similarities between every row in matrix_a
    and every row in matrix_b using matrix operations.
    
    matrix_a: shape (M, D)
    matrix_b: shape (N, D)
    returns: shape (M, N) matrix where entry (i, j) is sim(A[i], B[j])
    """
    # 1. Calculate L2 norm (magnitude) along rows for each matrix
    norm_a = np.linalg.norm(matrix_a, axis=1, keepdims=True)  # Shape: (M, 1)
    norm_b = np.linalg.norm(matrix_b, axis=1, keepdims=True)  # Shape: (N, 1)
    
    # 2. Normalize matrices to unit length (length = 1.0)
    normalized_a = matrix_a / np.maximum(norm_a, 1e-10)
    normalized_b = matrix_b / np.maximum(norm_b, 1e-10)
    
    # 3. Matrix multiplication computes all pairwise dot products at once
    # Shape: (M, D) @ (D, N) -> (M, N)
    return normalized_a @ normalized_b.T

if __name__ == "__main__":
    # Document A (Long text about cats): High magnitude
    doc_a = [10.0, 20.0, 30.0]
    # Document B (Short text about cats): Low magnitude, some relative orientation
    doc_b = [1.0, 2.0, 3.0]
    # Document C (Unrelated text): Different relative direction
    doc_c = [5.0, -1.0, 0.0]
    print(f"Raw Dot Product (Doc A . Doc B): {dot_product(doc_a, doc_b)}")
    print(f"Cosine Similarity (Doc A, Doc B): {cosine_similarity(doc_a, doc_b):.4f}")
    print(f"Cosine Similarity (Doc A, Doc C): {cosine_similarity(doc_a, doc_c):.4f}")
