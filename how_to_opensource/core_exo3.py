import numpy as np
from numpy.typing import ArrayLike


def add_two_vectors(
    a: ArrayLike,
    b: ArrayLike
) -> ArrayLike:
    result: ArrayLike
    result = np.add(a, b)
    return result
