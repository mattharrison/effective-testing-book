import numpy as np

def safe_invert(X: np.ndarray) -> np.ndarray:
    if np.linalg.cond(X) > 1e12:
        raise ValueError("Matrix is near-singular")
    return np.linalg.inv(X)


import pytest
import numpy as np

@pytest.mark.parametrize("X", [
    np.eye(2),
    np.array([[1, 0], [0, 5]])
])
def test_safe_invert_valid(X):
    result = safe_invert(X)
    assert result.shape == X.shape
    np.testing.assert_allclose(X @ result, np.eye(X.shape[0]), atol=1e-8)

@pytest.mark.parametrize("X", [
    np.array([[1, 2], [2, 4]]),               # Singular due to linear dependency
    np.array([[1e12, 0], [0, 1e-12]])        # Nearly singular due to tiny values
])
def test_safe_invert_singular(X):
    with pytest.raises(ValueError):
        res = safe_invert(X)

def load_real_data() -> np.ndarray:
    # Simulate loading a real dataset that may be ill-conditioned
    return np.array([[1, 2, 3], [2, 4, 6], [3, 6, 9]])

@pytest.mark.xfail(reason="Matrix may be unstable in real-world data")
def test_real_data_invert():
    X = load_real_data()
    safe_invert(X)
