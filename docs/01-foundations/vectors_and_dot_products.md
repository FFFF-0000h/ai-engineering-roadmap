1. Computer Scientist vs. Mathematician vs. Physicist:
    - Computer Scientist: A vector is an ordered array/list of numbers where index position has semantic meaning.

    - Mathematician / Geometer: A point or arrow in an $N$-dimensional space with both magnitude (length) and direction.

    - Physicist: A vector is an arrow or point that has both magnitude (length) and direction.

2. Geometric Meaning of the Dot Product:
    - The dot product measures directional alignment and scale.
    - If two vectors point in the exact same direction, their dot product is maximized.
    - If they are perpendicular ($90^\circ$ apart), their dot product is $0$.If they point in opposite directions, it is negative.

    Caveat: As you noticed with $32$ in the Python program, raw dot products depend heavily on the length of the vectors. If a vector is long, its dot product can be huge even if the direction is slightly off!

3. The formula for the dot product ($\mathbf{A} \cdot \mathbf{B} = \sum A_i B_i$).

