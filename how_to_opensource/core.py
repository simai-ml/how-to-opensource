import numpy as np

from typing import Any
from numpy.typing import ArrayLike

def add_two_vectors(
    a: ArrayLike,
    b: ArrayLike
) -> ArrayLike:
    """
    Sum two vectors.

    Parameters
    ----------
    a : ArrayLike
        First vector.
    b : ArrayLike
        Second vector.

    Returns
    -------
    ArrayLike
        Sum of the two inputs.

    Examples
    --------
        >>> from how_to_opensource import add_two_vectors
        >>> add_two_vectors([12.5, 26.1], [7.5, 3.9])
        array([20., 30.])
    """
    result: ArrayLike
    result = np.add(a, b)
    return result
