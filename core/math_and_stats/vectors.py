def dot_product(v1: list[float], v2: list[float]) -> float:
    """Calculates the dot product of two equal-length vectors."""
    if len(v1) != len(v2):
        raise ValueError("Vectors must be of identical length.")

    return sum(x * y for x, y in zip(v1, v2))

if __name__ == "__main__":
    a = [1.0, 2.0, 3.0]
    b = [4.0, 5.0, 6.0]
    print(f"Dot Product of {a} and {b}: {dot_product(a, b)}")
