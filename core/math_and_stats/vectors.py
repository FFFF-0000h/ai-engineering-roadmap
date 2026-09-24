import math

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
